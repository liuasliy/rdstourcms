# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from photo.models import *
from accounts.models import *
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import Http404
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404 
import json

# Create your views here.
def photopage(request):
    users = MyProfile.objects.all()
    photo_list = photoList.objects.order_by('-pubdate')

    # 总数据列表
    paginator = Paginator(photo_list, 25)

    page = request.GET.get('page')
    try:
        photos = paginator.page(page)
    except PageNotAnInteger:
        photos = paginator.page(1)
    except EmptyPage:
        photos = paginator.page(paginator.num_pages)

    return render_to_response('photo.html', {"photos": photos, "users": users}, context_instance=RequestContext(request))




def ajax_get_photo(request):
    info = {
            'name':'yihen',
            'age':18,
            'sex':'man'
    }
    my_json = json.dumps(info)
    return  HttpResponse(my_json, content_type="application/json")