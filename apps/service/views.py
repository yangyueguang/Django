from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
def index(request):
    result = {'ds':'中国'}
    # return HttpResponse(json.dumps())
    return HttpResponse(json.dumps(result,ensure_ascii=False),content_type="application/json,charset=utf-8")
    #return  render(request,'index.html')