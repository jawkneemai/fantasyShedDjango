from django.shortcuts import render
from django.http import HttpResponse

def index(request):
	return HttpResponse('yous at the landing page')


