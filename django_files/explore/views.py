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

def explore(request, entity_id):
   return render_to_response("organization.html", {'id': entity_id})
