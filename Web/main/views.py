from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return render(request,'base.html')

def team(request):
    return render(request,'team.html')

def NotFound(request, exception=None):
    return render(request,'404.html',status=404)