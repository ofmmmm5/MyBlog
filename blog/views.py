# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponseRedirect
from django.shortcuts import render
from . import models

# Create your views here.
def index(request):
    articles = models.Artical.objects.all
    return render(request, 'blog/index.html',{'articles' : articles})

def article_page(request,article_id):
    article = models.Artical.objects.get(pk = article_id)
    return render(request,'blog/article_page.html',{'article':article})

def edit_page(request,article_id):
    if str(article_id) == '0':
        return render(request,'blog/edit_page.html')
    article = models.Artical.objects.get(pk = article_id)
    return render(request,'blog/edit_page.html',{'article':article})

def edit_action(request):
    title = request.POST.get('Title','TITLE')
    content = request.POST.get('Content','CONTENT')
    id = request.POST.get('article_id','null')
    if(str(id) == 0):
        models.Artical.objects.create(title=title,content=content)
        return HttpResponseRedirect('/blog/index')
    else:
        article = models.Artical.objects.get(pk = id)
        article.title = title
        article.content = content
        article.save()
        return render(request,'blog/article_page.html',{'article':article})


def update(request,article_id):
    article = models.Artical.objects.get(pk=article_id)
    return render(request,'blog/update.html',{'article': article})

def update_action(request,article_id):
    title = request.POST.get('Title', 'TITLE')
    content = request.POST.get('Content', 'CONTENT')
    models.Artical.objects.filter(pk=article_id).update(content = content)
    models.Artical.objects.filter(pk=article_id).update(title=title)
    return HttpResponseRedirect('/blog/index')
