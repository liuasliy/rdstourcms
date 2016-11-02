# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from travels.models import *
from favourite.models import *
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
from django.shortcuts import render_to_response,get_object_or_404

# Create your views here.

def add_favorite(request, travels_id):

    if request.user.is_authenticated():
        user = request.user
        travels = Travels.objects.get(id=travels_id)
        if Favourite.objects.filter(user__username=user, travels=travels):
            return HttpResponse("<div style='text-align: center'>该文章您已经收藏过了!</div>")
        else:
            favourlist = Favourite(user=user, travels=travels)
            favourlist.save()
            return HttpResponse("<div style='text-align: center'>收藏成功!</div>")
    else:
        return HttpResponse("<div style='text-align: center'>请您登陆后再收藏!</div>")




def favourite_list(request,user):
    users = MyProfile.objects.all()
    try:
        favlist = Favourite.objects.filter(user__username=user)
    except Favourite.DoesNotExist:
        raise Http404
    return render_to_response('../templates/userena/fav_list.html', {'favlist' : favlist, 'users': users}, context_instance=RequestContext(request))




def deletefav(request, favourite_id):
    favourite = get_object_or_404(Favourite, pk=int(favourite_id))

    favourite.delete()
    author = request.user.username
    return HttpResponseRedirect('/favlist/'+author)