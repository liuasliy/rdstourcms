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
from django.http import JsonResponse

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


def photodetail(request, photos_id):
    users = MyProfile.objects.all()
    photoAll = photoList.objects.order_by('-pubdate')[:4]
    try:
        photos = photoList.objects.get(id=photos_id)
        photos.count_hit += 1
        photos.save()
    except photoList.DoesNotExist:
        raise Http404

    return render_to_response('photo-deils.html', {'photos': photos, "photoAll":photoAll, "users": users}, context_instance=RequestContext(request))

def ajax_get_photo(request):
    '''ajax请求数据'''
    users = MyProfile.objects.all()
    try:
        items = photoList.objects.all()
    except:
        items = []
    return render_to_response('ajax_get_photo.html', {'items': items, "users": users}, context_instance=RequestContext(request))


def like_photo(request,photos_id):
    p_id = None
    LIKED = '谢谢鼓励，但你已经赞过啦！'

    liked_post = request.session.get('liked')
    p_id = photos_id
    if p_id == liked_post:
        return HttpResponse(LIKED)
    photo = get_object_or_404(photoList, id=photos_id)
    photo.praise_num += 1
    likes =photo.praise_num
    photo.save()
    request.session['liked'] = p_id
    return HttpResponse('点赞成功！点赞数+%s' %likes)