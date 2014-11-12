from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, Http404, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.core.urlresolvers import resolve
from django.conf import settings
import json, math, random, pickle
from explore.models import *
from django.core.cache import cache, get_cache
import redis
import redis_cache
from redis_cache import get_redis_connection

def home(request):
   return render_to_response("home.html")

def explore(request, app_type, entity_id):
   if app_type == "profile":
      return explore_profile(entity_id, "bipartite_rank", -1)
   elif app_type == "network":
      return explore_network(entity_id)
   elif app_type == "ranking":
      return explore_ranking(entity_id)

def static(request, app_type, entity_id, plot_type, target_id):
   return explore_profile(entity_id, plot_type, target_id)

def explore_profile(entity_id, plot_type, target_id):
   entity = Entity.objects.get(id = entity_id)
   ranking = Ranking.objects.get(entity = entity_id)
   other_type1 = ""
   other_type2 = ""
   othertype = ""
   thirdtype = ""
   if plot_type == "bipartite":
      if target_id != -1:
         target = Entity.objects.get(id = target_id)
      if entity.type_of_entity == "IS":
         other_type1 = "Organizations"
         other_type2 = "Countries"
         if target_id != -1:
            if target.type_of_entity == "CO":
               othertype = "Countries"
               thirdtype = "Organizations"
            else:
               othertype = "Organizations"
               thirdtype = "Countries"
      elif entity.type_of_entity == "CO":
         other_type1 = "Organizations"
         other_type2 = "Issues"
         if target_id != -1:
            if target.type_of_entity == "IS":
               othertype = "Issues"
               thirdtype = "Organizations"
            else:
               othertype = "Organizations"
               thirdtype = "Issues"
      elif entity.type_of_entity == "OR":
         other_type1 = "Issues"
         other_type2 = "Countries"
         if target_id != -1:
            if target.type_of_entity == "CO":
               othertype = "Countries"
               thirdtype = "Issues"
            else:
               othertype = "Issues"
               thirdtype = "Countries"
   else:
      othertype = target_id
      if entity.type_of_entity == "IS":
         other_type1 = "Organizations"
         other_type2 = "Countries"
         if target_id == "Organizations":
            thirdtype = "Countries"
         else:
            thirdtype = "Organizations"
      elif entity.type_of_entity == "CO":
         other_type1 = "Organizations"
         other_type2 = "Issues"
         if target_id == "Organizations":
            thirdtype = "Issues"
         else:
            thirdtype = "Organizations"
      elif entity.type_of_entity == "OR":
         other_type1 = "Issues"
         other_type2 = "Countries"
         if target_id == "Issues":
            thirdtype = "Countries"
         else:
            thirdtype = "Issues"
   if plot_type == "bipartite_rank" and target_id == -1:
      target_id = other_type1
   issues = Entity.objects.filter(type_of_entity = "IS").order_by("name")
   for issue in issues:
      issue.name = issue.name.title()
   countries = Entity.objects.filter(type_of_entity = "CO").order_by("name")
   for country in countries:
      country.name = country.name.title()
   orgs = Entity.objects.filter(type_of_entity = "OR").order_by("name")
   for org in orgs:
      org.name = org.name.title()
   return render_to_response("profile.html", {
      'id': entity.id,
      'name': entity.name.title(),
      'type': entity.type_of_entity,
      'rank': ranking.rank,
      'consistency': ranking.consistency_value,
      'other_type1': other_type1,
      'other_type2': other_type2,
      'issues': issues,
      'countries': countries,
      'orgs': orgs,
      'issue_n': len(issues),
      'country_n': len(countries),
      'org_n': len(orgs),
      'plot_id': target_id,
      'plot_type': plot_type,
      'othertype': othertype,
      'thirdtype': thirdtype,
      'section': "profile",
   })

def explore_network(network_id):
   if network_id == "1":
      type = "OR"
   elif network_id == "2":
      type = "CO"
   else:
      type = "IS"
   return render_to_response("network.html", {
      'type': type,
      'section': "network",
   })

def explore_ranking(ranking_id):
   if ranking_id == "1":
      type = "OR"
   elif ranking_id == "2":
      type = "CO"
   else:
      type = "IS"
   ranks = Ranking.objects.filter(entity__type_of_entity = type).order_by('rank')
   rankings = []
   for rank in ranks:
      record = {}
      record["id"] = rank.entity.id
      record["name"] = rank.entity.name.title()
      record["value"] = rank.consistency_value
      record["rank"] = rank.rank
      rankings.append(record)
   return render_to_response("ranking.html", {
      'type': type,
      'rankings': rankings,
      'section': "ranking",
   })

def get_data(request, app_type, entity_id, data_type, target_id):
   if data_type == "bipartite":
      return get_data_bipartite(entity_id, target_id)
   elif data_type == "list":
      return get_data_list(entity_id, target_id)
   elif data_type == "network":
      return get_data_network(entity_id, target_id)
   elif data_type == "relations":
      return get_data_relations(entity_id, target_id)
   elif data_type == "bipartite_rank":
      return get_data_bipartite_rank(entity_id, target_id)
   elif data_type == "consistency":
      return get_data_consistency(entity_id, target_id)


def get_data_bipartite(entity_id, target_id):
   response_data = {}
   response_data["interpretation"] = "This <span class=\"glossaryterm\" title=\"Alignment Plot: Given two Entities, an Alignment Plot is a scatter gram of their Relevances. For example, in the Alignment Plot of Uganda and Agriculture, each data point is an organization and its coordinates in the scatter gram are obtained by checking its Relevance with Uganda and with Agriculture. The exponent of the slope of an Alignment Plot is called Alignment and we refer to it with the symbol &alpha;.\">plot</span> shows how "
   entity = Entity.objects.get(id = entity_id)
   target = Entity.objects.get(id = target_id)
   if (entity.type_of_entity == "IS") or (entity.type_of_entity == "OR" and target.type_of_entity == "CO"):
      target = Entity.objects.get(id = entity_id)
      entity = Entity.objects.get(id = target_id)
   if entity.type_of_entity == "CO":
      if target.type_of_entity == "IS":
         point_label = "organizations"
         response_data["x_axis"] = "How relevant is %s to the Organizations" % entity.name.title()
      elif target.type_of_entity == "OR":
         point_label = "issues"
         response_data["x_axis"] = "How relevant is %s to the Issues" % entity.name.title()
   elif entity.type_of_entity == "OR":
      if target.type_of_entity == "IS":
         point_label = "countries"
         response_data["x_axis"] = "How relevant is %s to the Countries" % entity.name.title()
   if target.type_of_entity == "IS":
      if entity.type_of_entity == "CO":
         response_data["y_axis"] = "How relevant is %s to the Organizations" % target.name.title()
      elif entity.type_of_entity == "OR":
         response_data["y_axis"] = "How relevant is %s to the Countries" % target.name.title()
   elif target.type_of_entity == "OR":
      if entity.type_of_entity == "CO":
         response_data["y_axis"] = "How relevant is %s to the Issues" % target.name.title()
   response_data["interpretation"] += "%s relate to %s and %s.<br />" % (point_label, entity.name.title(), target.name.title())
   response_data["points"] = []
   points_x = Bipartite.objects.filter(entity_src = entity.id)
   temp_records = {}
   min_x = 1000
   max_x = 0
   min_y = 1000
   max_y = 0
   for point in points_x:
      if point.entity_trg.type_of_entity != target.type_of_entity:
         record = {}
         record["x"] = point.rca
         record["size"] = point.hits
         temp_records[point.entity_trg.name] = record
      if int(point.entity_trg_id) == int(target.id) or int(point.entity_trg_id) == int(entity.id):
         rca = point.rca
         alpha = point.alpha
         beta = point.beta
   points_y = Bipartite.objects.filter(entity_src = target.id)
   for point in points_y:
      if point.entity_trg.type_of_entity != entity.type_of_entity and point.entity_trg.name in temp_records:
         record = {}
         record["id"] = point.entity_trg_id
         record["x"] = temp_records[point.entity_trg.name]["x"]
         if record["x"] > max_x:
            max_x = record["x"]
         elif record["x"] < min_x:
            min_x = record["x"]
         record["y"] = point.rca
         if point.rca > max_y:
            max_y = point.rca
         elif point.rca < min_y:
            min_y = point.rca
         record["size"] = point.hits + temp_records[point.entity_trg.name]["size"]
         record["label"] = point.entity_trg.name.title()
         response_data["points"].append(record)
   x1 = min_x
   x2 = max_x
   y1 = beta * math.pow(min_x, alpha)
   y2 = beta * math.pow(max_x, alpha)
   if y1 < min_y:
      y1 = min_y
      x1 = math.pow(y1 / beta, 1 / alpha)
   if y1 > max_y:
      y1 = max_y
      x1 = math.pow(y1 / beta, 1 / alpha)
   if y2 < min_y:
      y2 = min_y
      x2 = math.pow(y2 / beta, 1 / alpha)
   if y2 > max_y:
      y2 = max_y
      x2 = math.pow(y2 / beta, 1 / alpha)
   response_data["trendline"] = {}
   response_data["trendline"]["x1"] = x1
   response_data["trendline"]["y1"] = y1
   response_data["trendline"]["x2"] = x2
   response_data["trendline"]["y2"] = y2
   response_data["trendlabel"] = u"%s<br />%s<hr />\u03B1 = %1.4f" % (entity.name.title(), target.name.title(), alpha)
   response_data["plot_title"] = "R = %1.4f" % (rca)
   if rca > 1:
      response_data["interpretation"] += "We found that %s and %s are <span class=\"glossaryterm\" title=\"Relevance: How strong is the association between two Entities. Relevance is calculated by normalizing the number of documents that contain both Entities over the total number of documents retrieved. When the Relevance is higher than 1 we say that the two entities are Relevant for each other, otherwise they are not Relevant. For example, suppose we want to know the Relevance of World Bank for Lesotho. We know that World Bank and Lesotho appears in 1,000 documents, that World Bank alone appears in 1,000,000 documents, that Lesotho appears in 4,000 documents and that we retrieved a total of 3,000,000 documents. The 'World Bank - Lesotho' Relevance is then equal to (1,000 / 1,000,000) / (4,000 / 3,000,000) = .75.\">relevant</span> to each other in the aid community, as their R is greater than 1.<br />Therefore, %s <span class=\"glossaryterm\" title=\"Relevance: How strong is the association between two Entities. Relevance is calculated by normalizing the number of documents that contain both Entities over the total number of documents retrieved. When the Relevance is higher than 1 we say that the two entities are Relevant for each other, otherwise they are not Relevant. For example, suppose we want to know the Relevance of World Bank for Lesotho. We know that World Bank and Lesotho appears in 1,000 documents, that World Bank alone appears in 1,000,000 documents, that Lesotho appears in 4,000 documents and that we retrieved a total of 3,000,000 documents. The 'World Bank - Lesotho' Relevance is then equal to (1,000 / 1,000,000) / (4,000 / 3,000,000) = .75.\">relevant</span> for %s should also be <span class=\"glossaryterm\" title=\"Relevance: How strong is the association between two Entities. Relevance is calculated by normalizing the number of documents that contain both Entities over the total number of documents retrieved. When the Relevance is higher than 1 we say that the two entities are Relevant for each other, otherwise they are not Relevant. For example, suppose we want to know the Relevance of World Bank for Lesotho. We know that World Bank and Lesotho appears in 1,000 documents, that World Bank alone appears in 1,000,000 documents, that Lesotho appears in 4,000 documents and that we retrieved a total of 3,000,000 documents. The 'World Bank - Lesotho' Relevance is then equal to (1,000 / 1,000,000) / (4,000 / 3,000,000) = .75.\">relevant</span> for %s (upper-right quadrant) and %s not <span class=\"glossaryterm\" title=\"Relevance: How strong is the association between two Entities. Relevance is calculated by normalizing the number of documents that contain both Entities over the total number of documents retrieved. When the Relevance is higher than 1 we say that the two entities are Relevant for each other, otherwise they are not Relevant. For example, suppose we want to know the Relevance of World Bank for Lesotho. We know that World Bank and Lesotho appears in 1,000 documents, that World Bank alone appears in 1,000,000 documents, that Lesotho appears in 4,000 documents and that we retrieved a total of 3,000,000 documents. The 'World Bank - Lesotho' Relevance is then equal to (1,000 / 1,000,000) / (4,000 / 3,000,000) = .75.\">relevant</span> for %s should also not be <span class=\"glossaryterm\" title=\"Relevance: How strong is the association between two Entities. Relevance is calculated by normalizing the number of documents that contain both Entities over the total number of documents retrieved. When the Relevance is higher than 1 we say that the two entities are Relevant for each other, otherwise they are not Relevant. For example, suppose we want to know the Relevance of World Bank for Lesotho. We know that World Bank and Lesotho appears in 1,000 documents, that World Bank alone appears in 1,000,000 documents, that Lesotho appears in 4,000 documents and that we retrieved a total of 3,000,000 documents. The 'World Bank - Lesotho' Relevance is then equal to (1,000 / 1,000,000) / (4,000 / 3,000,000) = .75.\">relevant</span> for %s (lower-left quadrant).<br />" % (entity.name.title(), target.name.title(), point_label, entity.name.title(), target.name.title(), point_label, entity.name.title(), target.name.title())
      if alpha > 0:
         response_data["interpretation"] += u"And the aid community is <span class=\"glossaryterm\" title=\"Alignment (&alpha;): Two Entities are said to be Positively Aligned if their Relevance correlates. For example, Amnesty International is aligned with Human Rights if all organizations that are Relevant to Amnesty International are also Relevant to Human Rights. If the opposite holds, then the two Entities are said to be Negatively Aligned. Formally, the Alignment &alpha; is the exponent of the regression of a Alignment Plot.\">aligning</span> accordingly, as the \u03B1 is greater than 0. This is what we call a \"Positive Match\": most poinst lie in the correct quadrants.<br />"
      else:
         response_data["interpretation"] += u"However, the aid community is not <span class=\"glossaryterm\" title=\"Alignment (&alpha;): Two Entities are said to be Positively Aligned if their Relevance correlates. For example, Amnesty International is aligned with Human Rights if all organizations that are Relevant to Amnesty International are also Relevant to Human Rights. If the opposite holds, then the two Entities are said to be Negatively Aligned. Formally, the Alignment &alpha; is the exponent of the regression of a Alignment Plot.\">aligning</span> accordingly, as the \u03B1 is lower than 0. This is what we call a \"Mismatch\": most points lie in the upper-left or lower-right quadrant.<br />"
   else:
      response_data["interpretation"] += "We found that %s and %s are not <span class=\"glossaryterm\" title=\"Relevance: How strong is the association between two Entities. Relevance is calculated by normalizing the number of documents that contain both Entities over the total number of documents retrieved. When the Relevance is higher than 1 we say that the two entities are Relevant for each other, otherwise they are not Relevant. For example, suppose we want to know the Relevance of World Bank for Lesotho. We know that World Bank and Lesotho appears in 1,000 documents, that World Bank alone appears in 1,000,000 documents, that Lesotho appears in 4,000 documents and that we retrieved a total of 3,000,000 documents. The 'World Bank - Lesotho' Relevance is then equal to (1,000 / 1,000,000) / (4,000 / 3,000,000) = .75.\">relevant</span> for each other in the aid community, as their R is lower than 1.<br />Therefore, %s <span class=\"glossaryterm\" title=\"Relevance: How strong is the association between two Entities. Relevance is calculated by normalizing the number of documents that contain both Entities over the total number of documents retrieved. When the Relevance is higher than 1 we say that the two entities are Relevant for each other, otherwise they are not Relevant. For example, suppose we want to know the Relevance of World Bank for Lesotho. We know that World Bank and Lesotho appears in 1,000 documents, that World Bank alone appears in 1,000,000 documents, that Lesotho appears in 4,000 documents and that we retrieved a total of 3,000,000 documents. The 'World Bank - Lesotho' Relevance is then equal to (1,000 / 1,000,000) / (4,000 / 3,000,000) = .75.\">relevant</span> for %s should not be <span class=\"glossaryterm\" title=\"Relevance: How strong is the association between two Entities. Relevance is calculated by normalizing the number of documents that contain both Entities over the total number of documents retrieved. When the Relevance is higher than 1 we say that the two entities are Relevant for each other, otherwise they are not Relevant. For example, suppose we want to know the Relevance of World Bank for Lesotho. We know that World Bank and Lesotho appears in 1,000 documents, that World Bank alone appears in 1,000,000 documents, that Lesotho appears in 4,000 documents and that we retrieved a total of 3,000,000 documents. The 'World Bank - Lesotho' Relevance is then equal to (1,000 / 1,000,000) / (4,000 / 3,000,000) = .75.\">relevant</span> for %s (lower-right quadrant) and %s not <span class=\"glossaryterm\" title=\"Relevance: How strong is the association between two Entities. Relevance is calculated by normalizing the number of documents that contain both Entities over the total number of documents retrieved. When the Relevance is higher than 1 we say that the two entities are Relevant for each other, otherwise they are not Relevant. For example, suppose we want to know the Relevance of World Bank for Lesotho. We know that World Bank and Lesotho appears in 1,000 documents, that World Bank alone appears in 1,000,000 documents, that Lesotho appears in 4,000 documents and that we retrieved a total of 3,000,000 documents. The 'World Bank - Lesotho' Relevance is then equal to (1,000 / 1,000,000) / (4,000 / 3,000,000) = .75.\">relevant</span> for %s should be <span class=\"glossaryterm\" title=\"Relevance: How strong is the association between two Entities. Relevance is calculated by normalizing the number of documents that contain both Entities over the total number of documents retrieved. When the Relevance is higher than 1 we say that the two entities are Relevant for each other, otherwise they are not Relevant. For example, suppose we want to know the Relevance of World Bank for Lesotho. We know that World Bank and Lesotho appears in 1,000 documents, that World Bank alone appears in 1,000,000 documents, that Lesotho appears in 4,000 documents and that we retrieved a total of 3,000,000 documents. The 'World Bank - Lesotho' Relevance is then equal to (1,000 / 1,000,000) / (4,000 / 3,000,000) = .75.\">relevant</span> for %s (upper-left quadrant).<br />" % (entity.name.title(), target.name.title(), point_label, entity.name.title(), target.name.title(), point_label, entity.name.title(), target.name.title())
      if alpha > 0:
         response_data["interpretation"] += u"However, the aid community is not <span class=\"glossaryterm\" title=\"Alignment (&alpha;): Two Entities are said to be Positively Aligned if their Relevance correlates. For example, Amnesty International is aligned with Human Rights if all organizations that are Relevant to Amnesty International are also Relevant to Human Rights. If the opposite holds, then the two Entities are said to be Negatively Aligned. Formally, the Alignment &alpha; is the exponent of the regression of a Alignment Plot.\">aligning</span> accordingly, as the \u03B1 is greater than 0. This is what we call a \"Mismatch\": most points lie in the upper-right or lower-left quadrant.<br />"
      else:
         response_data["interpretation"] += u"And the aid community is <span class=\"glossaryterm\" title=\"Alignment (&alpha;): Two Entities are said to be Positively Aligned if their Relevance correlates. For example, Amnesty International is aligned with Human Rights if all organizations that are Relevant to Amnesty International are also Relevant to Human Rights. If the opposite holds, then the two Entities are said to be Negatively Aligned. Formally, the Alignment &alpha; is the exponent of the regression of a Alignment Plot.\">aligning</span> accordingly, as the \u03B1 is lower than 0. This is what we call a \"Negative Match\": most poinst lie in the correct quadrants.<br />"
   return HttpResponse(json.dumps(response_data), mimetype="application/json")

def get_data_list(entity_id, list_type):
   if list_type == "Organizations":
      list_type = "OR"
   elif list_type == "Countries":
      list_type = "CO"
   elif list_type == "Issues":
      list_type = "IS"
   entity_list = Bipartite.objects.filter(entity_src = entity_id).filter(entity_trg__type_of_entity = list_type).order_by('entity_trg__name')
   response_data = []
   for entity in entity_list:
      record = {}
      record["id"] = entity.entity_trg.id
      record["name"] = entity.entity_trg.name.title()
      response_data.append(record)
   return HttpResponse(json.dumps(response_data), mimetype="application/json")

def get_data_network(network_id, entity_type):
   response_data = {}
   response_data["nodes"] = []
   raw = get_redis_connection('default')
   key = "network:%s:nodes" % (network_id)
   cache_query = raw.hget(key, 'data')
   if cache_query == None:
      nodes = Entity.objects.filter(type_of_entity = entity_type)
      raw.hset(key, 'data', pickle.dumps(nodes))
   else:
      encoded = cache_query
      decoded = pickle.loads(encoded)
      nodes = decoded
   nodemap = {}
   i = 0
   for node in nodes:
      if node.id == 250 or node.id == 254:
         continue
      nodemap[node.id] = i
      i += 1
      record = {}
      record["name"] = node.name.title()
      if node.type_of_entity == "OR":
         record["type"] = node.entropy
      else:
         record["type"] = node.subtype
      record["size"] = node.size
      record["system_id"] = node.id
      record["fixed"] = True
      record["x"] = node.x
      record["y"] = node.y
      response_data["nodes"].append(record)
   response_data["links"] = []
   key = "network:%s:edges" % (network_id)
   cache_query = raw.hget(key, 'data')
   if cache_query == None:
      edges = Edge.objects.filter(type = network_id)
      raw.hset(key, 'data', pickle.dumps(edges))
   else:
      encoded = cache_query
      decoded = pickle.loads(encoded)
      edges = decoded
   for edge in edges:
      record = {}
      record["source"] = nodemap[edge.entity_src.id]
      record["target"] = nodemap[edge.entity_trg.id]
      record["weight"] = edge.weight
      response_data["links"].append(record)
   return HttpResponse(json.dumps(response_data), mimetype="application/json")

def get_data_relations(entity_id, type_filter):
   if type_filter == "all":
      relations = Bipartite.objects.filter(entity_src = entity_id).order_by('entity_trg__name')
   else:
      if type_filter == "Organizations":
         type_code = "OR"
      if type_filter == "Countries":
         type_code = "CO"
      if type_filter == "Issues":
         type_code = "IS"
      relations = Bipartite.objects.filter(entity_src = entity_id).filter(entity_trg__type_of_entity = type_code).order_by('entity_trg__name')
   response_data = []
   for relation in relations:
      record = {}
      record["id"] = relation.entity_trg_id
      record["name"] = relation.entity_trg.name
      record["rca"] = relation.rca
      response_data.append(record)
   return HttpResponse(json.dumps(response_data), mimetype="application/json")

def get_data_bipartite_rank(entity_id, type_filter):
   if type_filter == "Organizations":
      type_code = "OR"
   if type_filter == "Countries":
      type_code = "CO"
   if type_filter == "Issues":
      type_code = "IS"
   ranks = Bipartite.objects.filter(entity_src = entity_id).filter(entity_trg__type_of_entity = type_code).order_by('-rca')
   response_data = {}
   response_data["points"] = []
   first = ""
   for rank in ranks:
      entity_name = rank.entity_src.name.title()
      record = {}
      record["id"] = rank.entity_trg_id
      record["name"] = rank.entity_trg.name.title()
      record["rca"] = rank.rca
      response_data["points"].append(record)
      if first == "":
         first = record["name"]
   response_data["interpretation"] = "This page shows the %s more related to %s.<br />The R value measures the relevance of the %s.<br />%s with R greater than 1, such as %s, are said to be relevant for %s.<br />%s with R lower than 1, such as %s, are said to be not relevant to %s." % (type_filter, entity_name, type_filter, type_filter, first, entity_name, type_filter, record["name"], entity_name)
   return HttpResponse(json.dumps(response_data), mimetype="application/json")

def get_data_consistency(entity_id, type_filter):
   response_data = {}
   if type_filter == "Organizations":
      type_code = "OR"
   if type_filter == "Countries":
      type_code = "CO"
   if type_filter == "Issues":
      type_code = "IS"
   points = Bipartite.objects.filter(entity_src = entity_id).filter(entity_trg__type_of_entity = type_code)
   response_data["x_axis"] = "How related are the %s to %s" % (type_filter, points[0].entity_src.name)
   response_data["y_axis"] = "How aligned are the %s to %s" % (type_filter, points[0].entity_src.name)
   response_data["points"] = []
   for point in points:
      record = {}
      record["id"] = point.entity_trg_id
      record["label"] = point.entity_trg.name.title()
      record["x"] = point.rca
      record["y"] = point.alpha
      record["size"] = point.hits
      response_data["points"].append(record)
   response_data["interpretation"] = "This page shows the <span class=\"glossaryterm\" title=\"Consistency Plot: Given an Entity, a Consistency Plot is a scatter gram of the Relevance against the Alignment. Each Entity has two Consistency Plots. For example, Doctors Without Borders has an Issue Consistency Plot and a Country Consistency Plot. In the Issue Consistency Plot, each data point is an issue and its coordinates in the scatter gram are obtained by checking its Relevance and its Alignment to Doctor Without Borders.\">consistency plot</span> of %s.<br />In the upper-left and lower-right quadrants we have the %s well <span class=\"glossaryterm\" title=\"Alignment (&alpha;): Two Entities are said to be Positively Aligned if their Relevance correlates. For example, Amnesty International is aligned with Human Rights if all organizations that are Relevant to Amnesty International are also Relevant to Human Rights. If the opposite holds, then the two Entities are said to be Negatively Aligned. Formally, the Alignment &alpha; is the exponent of the regression of a Alignment Plot.\">aligned</span> to %s.<br />In the lower-left and top-right quadrants we have the %s that are not <span class=\"glossaryterm\" title=\"Alignment (&alpha;): Two Entities are said to be Positively Aligned if their Relevance correlates. For example, Amnesty International is aligned with Human Rights if all organizations that are Relevant to Amnesty International are also Relevant to Human Rights. If the opposite holds, then the two Entities are said to be Negatively Aligned. Formally, the Alignment &alpha; is the exponent of the regression of a Alignment Plot.\">aligned</span> for %s.<br />" % (point.entity_src.name.title(), type_filter, point.entity_src.name.title(), type_filter, point.entity_src.name.title())
   return HttpResponse(json.dumps(response_data), mimetype="application/json")


def about(request, about_type):
   if about_type == "self":
      return render_to_response("about.html", {
         "section": "about",
      })
   elif about_type == "data":
      orgs = Entity.objects.filter(type_of_entity = "OR")
      return render_to_response("about_data.html", {
         "entities": orgs,
         "head": "Organization",
         "type": "data",
         "section": "about",
      })
   elif about_type == "data_cou":
      countries = Entity.objects.filter(type_of_entity = "CO")
      return render_to_response("about_data.html", {
         "entities": countries,
         "head": "Country",
         "type": "data",
         "section": "about",
      })
   elif about_type == "data_iss":
      issues = Entity.objects.filter(type_of_entity = "IS")
      return render_to_response("about_data.html", {
         "entities": issues,
         "head": "Issue",
         "type": "data",
         "section": "about",
      })
   elif about_type == "data_api":
      return render_to_response("about_data.html", {
         "type": "api",
         "section": "about",
      })
   elif about_type == "team":
      return render_to_response("about_team.html", {
         "section": "about",
      })
   elif about_type == "glossary":
      return render_to_response("about_glossary.html", {
         "section": "about",
      })

"""
def question(request):
   response_data = {}
   question_id = random.randint(1, 303)
   if question_id < 298:
      entity = Entity.objects.get(id = question_id)
      possible_ids = Bipartite.objects.filter(entity_src = question_id).order_by('?')
      question_id_2 = random.randint(1, len(possible_ids) + 4)
      if question_id_2 <= len(possible_ids):
         response_data["aText"] = "How does %s relate to %s?" % (entity.name.title(), possible_ids[0].entity_trg.name.title())
         response_data["hrefText"] = "static/profile/%d/bipartite/%d" % (entity.id, possible_ids[0].entity_trg.id)
      elif question_id_2 == (len(possible_ids) + 1):
         if entity.type_of_entity != "OR":
            response_data["aText"] = "How does %s relate to all Organizations?" % entity.name.title()
            response_data["hrefText"] = "static/profile/%d/consistency/Organizations/" % entity.id
         else:
            response_data["aText"] = "How does %s relate to all Countries?" % entity.name.title()
            response_data["hrefText"] = "static/profile/%d/consistency/Countries/" % entity.id
      elif question_id_2 == (len(possible_ids) + 2):
         if entity.type_of_entity != "IS":
            response_data["aText"] = "How does %s relate to all Issues?" % entity.name.title()
            response_data["hrefText"] = "static/profile/%d/consistency/Issues/" % entity.id
         else:
            response_data["aText"] = "How does %s relate to all Countries?" % entity.name.title()
            response_data["hrefText"] = "static/profile/%d/consistency/Countries/" % entity.id
      elif question_id_2 == (len(possible_ids) + 3):
         if entity.type_of_entity != "OR":
            response_data["aText"] = "What are the Organizations more related to %s?" % entity.name.title()
            response_data["hrefText"] = "static/profile/%d/bipartite_rank/Organizations/" % entity.id
         else:
            response_data["aText"] = "What are the Countries more related to %s?" % entity.name.title()
            response_data["hrefText"] = "static/profile/%d/bipartite_rank/Countries/" % entity.id
      elif question_id_2 == (len(possible_ids) + 4):
         if entity.type_of_entity != "IS":
            response_data["aText"] = "What are the Issues more related to %s?" % entity.name.title()
            response_data["hrefText"] = "static/profile/%d/bipartite_rank/Issues/" % entity.id
         else:
            response_data["aText"] = "What are the Countries more related to %s?" % entity.name.title()
            response_data["hrefText"] = "static/profile/%d/bipartite_rank/Countries/" % entity.id
   elif question_id == 298:
      response_data["aText"] = "What Aid Organization is related to each other Aid Organization?"
      response_data["hrefText"] = "network/1/"
   elif question_id == 299:
      response_data["aText"] = "What Country is related to each other Country for the Aid Organizations?"
      response_data["hrefText"] = "network/2/"
   elif question_id == 300:
      response_data["aText"] = "What Issue is related to each other Issue according to the Aid Organization?"
      response_data["hrefText"] = "network/3/"
   elif question_id == 301:
      response_data["aText"] = "What Aid Organization is more consistent in the Countries it is serving?"
      response_data["hrefText"] = "ranking/1/"
   elif question_id == 302:
      response_data["aText"] = "What Country is more consistent in the Issues it is served on?"
      response_data["hrefText"] = "ranking/2/"
   elif question_id == 303:
      response_data["aText"] = "What Issue is served more consistently by the Aid Organizations?"
      response_data["hrefText"] = "ranking/3/"
   return HttpResponse(json.dumps(response_data), mimetype="application/json")
"""
