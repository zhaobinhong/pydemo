# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .models import Article
from datetime import datetime
from django.contrib import admin
from django.http import Http404


# Create your views here.

# def detail(request, my_args):
#     post = Article.objects.all()[int(my_args)]
#     str = (
#         'title = %s,category = %s,date_time = %s,content = %s' % (
#             post.title, post.category, post.date_time, post.content))
#     return HttpResponse(str)


def index(request):
    h1 = u"个人主页"
    email = u"zhaobinhong@bankeys.com"
    title = u"主页"
    content = u"这是我的主页"
    dateTime = datetime.now()
    return render(request, "index.html", locals())


def home(request):
    post_list = Article.objects.all()  # 获取全部的Article对象
    return render(request, 'home.html', {'post_list': post_list})


def bowen(request):
    post_list = Article.objects.all()
    current_time = datetime.now()
    return render(request, 'home.html', locals())


def jineng(request):
    post_list = Article.objects.all()
    return render(request, 'jineng.html', locals())


def detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
        date_time = datetime.now()
        return render(request, "post.html", locals())
    except Article.DoesNotExist:
        raise Http404


def search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if not s:
            return render(request, 'home.html')
        else:
            post_list = Article.objects.filter(title__icontains=s)
            if len(post_list) == 0:
                return render(request, 'archives.html', {"post_list": post_list, 'error': True})
            else:
                return render(request, 'archives.html', {'post_list': post_list, 'error': False})

