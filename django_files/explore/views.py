from django.shortcuts import render_to_response, redirect
from django.http import HttpResponse, Http404, HttpResponsePermanentRedirect, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from django.template import RequestContext
from django.core.urlresolvers import resolve
from django.conf import settings
import json
from explore.models import *

def home(request):
   return render_to_response("home.html")

def explore(request, app_type, entity_id):
   if app_type == "profile":
      return explore_profile(entity_id)
   elif app_type == "network":
      return explore_network(entity_id)
   elif app_type == "ranking":
      return explore_ranking(entity_id)

def explore_profile(entity_id):
   entity = Entity.objects.get(id = entity_id)
   ranking = Ranking.objects.get(entity = entity_id)
   if entity.type_of_entity == "IS":
      other_type1 = "Organizations"
      other_type2 = "Countries"
   elif entity.type_of_entity == "CO":
      other_type1 = "Organizations"
      other_type2 = "Issues"
   elif entity.type_of_entity == "OR":
      other_type1 = "Issues"
      other_type2 = "Countries"
   return render_to_response("profile.html", {
      'id': entity.id,
      'name': entity.name,
      'type': entity.type_of_entity,
      'rank': ranking.rank,
      'consistency': ranking.consistency_value,
      'other_type1': other_type1,
      'other_type2': other_type2,
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
   return render_to_response("ranking.html", {
      'type': type,
      'rankings': ranks,
   })

def get_data(request, app_type, entity_id, data_type, target_id):
   if data_type == "bipartite":
      return get_data_bipartite(entity_id, target_id)
   elif data_type == "list":
      return get_data_list(target_id)
   elif data_type == "network":
      return get_data_network(entity_id, target_id)

def get_data_bipartite(entity_id, target_id):
   entity = Entity.objects.get(id = entity_id)
   target = Entity.objects.get(id = target_id)
   response_data = {}
   response_data["points"] = []
   points_x = Bipartite.objects.filter(entity_src = entity_id)
   temp_records = {}
   for point in points_x:
      if point.entity_trg.type_of_entity != target.type_of_entity:
         record = {}
         record["x"] = point.rca
         temp_records[point.entity_trg.name] = record
   points_y = Bipartite.objects.filter(entity_src = target_id)
   for point in points_y:
      if point.entity_trg.type_of_entity != entity.type_of_entity and point.entity_trg.name in temp_records:
         record = {}
         record["x"] = temp_records[point.entity_trg.name]["x"]
         record["y"] = point.rca
         record["label"] = point.entity_trg.name
         response_data["points"].append(record)
   return HttpResponse(json.dumps(response_data), mimetype="application/json")

def get_data_list(list_type):
   if list_type == "Organizations":
      list_type = "OR"
   elif list_type == "Countries":
      list_type = "CO"
   elif list_type == "Issues":
      list_type = "IS"
   entity_list = Entity.objects.filter(type_of_entity = list_type).order_by('name')
   response_data = []
   for entity in entity_list:
      record = {}
      record["id"] = entity.id
      record["name"] = entity.name.capitalize()
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
      record["name"] = node.name
      if node.type_of_entity == "OR":
         record["type"] = node.entropy
      else:
         record["type"] = node.subtype
      record["size"] = node.size
      record["system_id"] = node.id
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

def about(request, about_type):
   if about_type == "self":
      return render_to_response("about.html")
   elif about_type == "data":
      return render_to_response("about_data_org.html")
   elif about_type == "team":
      return render_to_response("about_team.html")
