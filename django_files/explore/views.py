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

def get_data(request, app_type, entity_id, data_type, target_id):
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

def get_list(request, app_type, entity_id, data_type, list_type):
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
