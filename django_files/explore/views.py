from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, Http404, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.core.urlresolvers import resolve
from django.conf import settings
import json, math, random
from explore.models import *

def home(request):
   return render_to_response("home.html")

def explore(request, app_type, entity_id):
   if app_type == "profile":
      return explore_profile(entity_id, "bipartite", -1)
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
   entity = Entity.objects.get(id = entity_id)
   target = Entity.objects.get(id = target_id)
   if (entity.type_of_entity == "IS") or (entity.type_of_entity == "OR" and target.type_of_entity == "CO"):
      target = Entity.objects.get(id = entity_id)
      entity = Entity.objects.get(id = target_id)
   if entity.type_of_entity == "CO":
      response_data["x_axis"] = "Country R"
      if target.type_of_entity == "IS":
         response_data["x_tooltip"] = "How much the Organizations are related to %s" % entity.name
      elif target.type_of_entity == "OR":
         response_data["x_tooltip"] = "How much the Issues are related to %s" % entity.name
   elif entity.type_of_entity == "OR":
      response_data["x_axis"] = "Organization R"
      if target.type_of_entity == "IS":
         response_data["x_tooltip"] = "How much the Countries are related to %s" % entity.name
   if target.type_of_entity == "IS":
      response_data["y_axis"] = "Issue R"
      if entity.type_of_entity == "CO":
         response_data["y_tooltip"] = "How much the Organizations are related to %s" % target.name
      elif entity.type_of_entity == "OR":
         response_data["y_tooltip"] = "How much the Countries are related to %s" % target.name
   elif target.type_of_entity == "OR":
      response_data["y_axis"] = "Organization R"
      if entity.type_of_entity == "CO":
         response_data["y_tooltip"] = "How much the Issues are related to %s" % target.name
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
         if point.rca > max_x:
            max_x = point.rca
         elif point.rca < min_x:
            min_x = point.rca
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
   nodes = Entity.objects.filter(type_of_entity = entity_type)
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
   edges = Edge.objects.filter(type = network_id)
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
   response_data = []
   for rank in ranks:
      record = {}
      record["id"] = rank.entity_trg_id
      record["name"] = rank.entity_trg.name.title()
      record["rca"] = rank.rca
      response_data.append(record)
   return HttpResponse(json.dumps(response_data), mimetype="application/json")

def get_data_consistency(entity_id, type_filter):
   response_data = {}
   if type_filter == "Organizations":
      type_code = "OR"
      response_data["x_axis"] = "Organization R"
      response_data["y_axis"] = u"Organization \u03B1"
   if type_filter == "Countries":
      type_code = "CO"
      response_data["x_axis"] = "Country R"
      response_data["y_axis"] = u"Country \u03B1"
   if type_filter == "Issues":
      type_code = "IS"
      response_data["x_axis"] = "Issue R"
      response_data["y_axis"] = u"Issue \u03B1"
   points = Bipartite.objects.filter(entity_src = entity_id).filter(entity_trg__type_of_entity = type_code)
   response_data["x_tooltip"] = "How related are the %s to %s" % (type_filter, points[0].entity_src.name)
   response_data["y_tooltip"] = "How aligned are the %s to %s" % (type_filter, points[0].entity_src.name)
   response_data["points"] = []
   for point in points:
      record = {}
      record["id"] = point.entity_trg_id
      record["label"] = point.entity_trg.name.title()
      record["x"] = point.rca
      record["y"] = point.alpha
      record["size"] = point.hits
      response_data["points"].append(record)
   return HttpResponse(json.dumps(response_data), mimetype="application/json")


def about(request, about_type):
   if about_type == "self":
      return render_to_response("about.html")
   elif about_type == "data":
      orgs = Entity.objects.filter(type_of_entity = "OR")
      return render_to_response("about_data.html", {
         "entities": orgs,
         "head": "Organization",
         "type": "data",
      })
   elif about_type == "data_cou":
      countries = Entity.objects.filter(type_of_entity = "CO")
      return render_to_response("about_data.html", {
         "entities": countries,
         "head": "Country",
         "type": "data",
      })
   elif about_type == "data_iss":
      issues = Entity.objects.filter(type_of_entity = "IS")
      return render_to_response("about_data.html", {
         "entities": issues,
         "head": "Issue",
         "type": "data",
      })
   elif about_type == "data_api":
      return render_to_response("about_data.html", {
         "type": "api",
      })
   elif about_type == "team":
      return render_to_response("about_team.html")

def question(request):
   response_data = {}
   question_id = random.randint(1, 303)
   if question_id < 298:
      entity = Entity.objects.get(id = question_id)
      possible_ids = Bipartite.objects.filter(entity_src = question_id).order_by('?')
      question_id_2 = random.randint(1, len(possible_ids) + 4)
      if question_id_2 <= len(possible_ids):
         response_data["aText"] = "How does %s relate to %s?" % (entity.name.title(), possible_ids[0].entity_trg.name.title())
         response_data["hrefText"] = "profile/%d/bipartite/%d" % (entity.id, possible_ids[0].entity_trg.id)
      elif question_id_2 == (len(possible_ids) + 1):
         if entity.type_of_entity != "OR":
            response_data["aText"] = "How does %s relate to all Organizations?" % entity.name.title()
            response_data["hrefText"] = "profile/%d/consistency/Organizations/" % entity.id
         else:
            response_data["aText"] = "How does %s relate to all Countries?" % entity.name.title()
            response_data["hrefText"] = "profile/%d/consistency/Countries/" % entity.id
      elif question_id_2 == (len(possible_ids) + 2):
         if entity.type_of_entity != "IS":
            response_data["aText"] = "How does %s relate to all Issues?" % entity.name.title()
            response_data["hrefText"] = "profile/%d/consistency/Issues/" % entity.id
         else:
            response_data["aText"] = "How does %s relate to all Countries?" % entity.name.title()
            response_data["hrefText"] = "profile/%d/consistency/Countries/" % entity.id
      elif question_id_2 == (len(possible_ids) + 3):
         if entity.type_of_entity != "OR":
            response_data["aText"] = "What are the Organizations more related to %s?" % entity.name.title()
            response_data["hrefText"] = "profile/%d/bipartite_rank/Organizations/" % entity.id
         else:
            response_data["aText"] = "What are the Countries more related to %s?" % entity.name.title()
            response_data["hrefText"] = "profile/%d/bipartite_rank/Countries/" % entity.id
      elif question_id_2 == (len(possible_ids) + 4):
         if entity.type_of_entity != "IS":
            response_data["aText"] = "What are the Issues more related to %s?" % entity.name.title()
            response_data["hrefText"] = "profile/%d/bipartite_rank/Issues/" % entity.id
         else:
            response_data["aText"] = "What are the Countries more related to %s?" % entity.name.title()
            response_data["hrefText"] = "profile/%d/bipartite_rank/Countries/" % entity.id
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
