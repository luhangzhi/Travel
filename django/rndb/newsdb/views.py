#coding:utf-8
from django.shortcuts import render
import json
from django.shortcuts import redirect
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.forms import ModelForm
from django.contrib import auth
from django.contrib.auth.models import User

from newsdb.models import scenic
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers import serialize,deserialize
from django.db.models.query import QuerySet
from dss.Serializer import serializer
# Create your views here.

def getscenic(request,place):
	if request.method == 'GET':
		print(place)
		print("get scenic")
		list=scenic.objects.filter(area__contains=place)
		datat=serializer(list,output_type = 'json')
		return HttpResponse(datat,content_type="application/json")

def getbyID(request,sid):
	if request.method == 'GET':
		print(sid)
		list=scenic.objects.filter(id=sid)
		print(list)
		datat=serializer(list,output_type='json')
		return HttpResponse(datat,content_type="application/json")

