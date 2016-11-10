# coding:utf-8
from django.shortcuts import render

# Create your views here.

def index(request):
    title=u"主页"
    content=u"这是我的主页"
    return render(request,"index.html",locals())