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
