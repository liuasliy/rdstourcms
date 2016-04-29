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

# Create your views here.

def favlist(request):
    users = MyProfile.objects.all()
    try:
        list = Favourite.objects.all()
    except Favourite.DoesNotExist:
        raise Http404
    return render_to_response('../templates/userena/fav_list.html', {'list' : list, 'users':users}, context_instance=RequestContext(request))

