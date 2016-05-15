# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from travels.models import *
from photo.models import *
from accounts.models import *
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import Http404
import time
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail
from django.utils import timezone
import datetime

# Create your views here.
def index(request):
    '''
    首页
    '''
    travels = Travels.objects.order_by('-pub_date')[:3]
    photos = photoList.objects.order_by('-pubdate')[:10]
    return render_to_response('index.html', {"travels": travels, "photos": photos}, context_instance=RequestContext(request))


#用户信息预览
def accountview(request, author_id):
    users = User.objects.all()

    try:
        useritem = MyProfile.objects.filter(user_id__exact=author_id)


        travelslist = Travels.objects.filter(author_id__iexact=author_id)
        photolist = photoList.objects.filter(user__id__iexact=author_id)
    except Travels.DoesNotExist:
        raise Http404


    return  render_to_response('account-views.html',
                               {"travelslist": travelslist,
                                "photolist": photolist,
                                "users": users,
                                "useritem": useritem
                                }, context_instance=RequestContext(request))







