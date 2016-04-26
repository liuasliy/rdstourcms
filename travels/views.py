# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from travels.models import *
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

def archive(request):
    travels = Travels.objects.all()
    users = MyProfile.objects.all()
    user = request.user
    travels_list = Travels.objects.order_by('-pub_date')

    # 总数据列表
    paginator = Paginator(travels_list, 25)

    page = request.GET.get('page')
    try:
        travels = paginator.page(page)
    except PageNotAnInteger:
        travels = paginator.page(1)
    except EmptyPage:
        travels = paginator.page(paginator.num_pages)

    return render_to_response('travels.html', {"travels": travels, "user": user, "users": users}, context_instance=RequestContext(request))


def detail(request, travels_id):
    users = MyProfile.objects.all()
    travelsall = Travels.objects.all()
    try:
        travels = Travels.objects.get(id=travels_id)


        travels.count_hit += 1
        travels.save()
    except Travels.DoesNotExist:
        raise Http404
    return render_to_response('travelsdetails.html', {"travels": travels,  "users": users, "travelsall": travelsall}, context_instance=RequestContext(request))


def uploadimage(request):
    if request.method == 'POST':
        callback = request.GET.get('CKEditorFuncNum')
        try:
            path = "media/upload/" + time.strftime("%Y%m%d%H%M%S", time.localtime())
            f = request.FILES["upload"]
            file_name = path + "_" + f.name
            des_origin_f = open(file_name, "wb+")
            for chunk in f:
                des_origin_f.write(chunk)
            des_origin_f.close()
        except Exception, e:
            print e
        res = r"<script>window.parent.CKEDITOR.tools.callFunction("+callback+",'/"+file_name+"', '');</script>"
        return HttpResponse(res)
    else:
        raise Http404()

# 登录视图:
# @csrf_exempt
def login(request):
    errors = []
    register_flag = False
    redirect_to = request.REQUEST.get('next', '')
    if request.method == "POST":
        if not request.POST.get('username', ''):
            errors.append(u"请输入用户名")
        if not request.POST.get('password', ''):
            errors.append(u"请输入密码")
        else:
            name = request.POST.get('username', '')
            password = request.POST.get('password', '')
            user = auth.authenticate(username=name, password=password)
            if user is not None and user.is_active:
                auth.login(request, user)
                return HttpResponseRedirect(redirect_to)
            else:
                errors.append(u'登录失败，请重试')
    response = render_to_response('login.html', {'errors': errors, },
        context_instance=RequestContext(request))
    return render(request, 'login.html', locals())

def logout(request):
    redirect_to = request.REQUEST.get('next', '')
    if request.user.is_authenticated():
        auth.logout(request)
        return render(request, "logout.html", {'redirect_to':redirect_to})
    else:
        return HttpResponseRedirect(redirect_to)



# 注册视图
from django.contrib.auth.models import User

@csrf_exempt
def register(request):
    errors=[]
    if request.method == 'POST':
        name = request.POST.get('username', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        if len(name) < 3:
            errors.append(u'用户名长度必须大于4个字符')
        elif len(password1) < 6:
            errors.append(u'密码长度必须大于6个字符')
        elif password1 != password2 :
            errors.append(u'两次输入密码必须相同')
        else:
            try:
                user = User.objects.get(username=name)
                errors.append(u'用户名已被注册')
                return render(request,'register.html',{'errors':errors})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username = name,
                    password = password1,
                    )
                register_flag = True
                return render(request,'login.html',{'register_flag':register_flag})
        return render(request,'register.html',{'errors':errors})
    else:
        return render(request,'register.html')


# 搜索
def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append(u'请填写查询内容！')
        elif len(q) > 50:
            errors.append(u'填写内容必须小于50字！')
        else:
            travels = Travels.objects.filter(title__icontains=q)
            
            return render_to_response('search.html',
                                      {'travels': travels, 'q': q}, context_instance=RequestContext(request))
    return render_to_response('search.html', {'errors': errors},
                              context_instance=RequestContext(request))


# 城市归类
def search_city(request, city):
    users = MyProfile.objects.all()
    try:
        travels_list = Travels.objects.filter(city__iexact=city)
    except Travels.DoesNotExist:
        raise Http404
    return render_to_response('city.html', {'travels_list' : travels_list, 'users':users}, context_instance=RequestContext(request))




from travels.forms import *
from django.core.urlresolvers import reverse
def list(request, author):
    users = MyProfile.objects.all()
    try:
        list = Travels.objects.filter(author__iexact=author)
    except Travels.DoesNotExist:
        raise Http404
    return render_to_response('../templates/userena/tra_list.html', {'list' : list, 'users':users}, context_instance=RequestContext(request))


# 新增:
@csrf_exempt
def add(request):
    user = request.user
    if request.method == "POST":
        uf = UserForm(request.POST, request.FILES)
        if uf.is_valid():
            title = uf.cleaned_data['title']
            content = uf.cleaned_data['content']
            contextinfo = uf.cleaned_data['contextinfo']
            image = uf.cleaned_data['image']
            bigimage = uf.cleaned_data['bigimage']
            city = uf.cleaned_data['city']
            author = request.user.username
            author_id = request.user.id
            travels = Travels()
            travels.title = title
            travels.content = content
            travels.contextinfo = contextinfo
            travels.image = image
            travels.bigimage = bigimage
            travels.city = city
            travels.author = author
            travels.author_id = author_id
            travels.save()
            return HttpResponseRedirect('/list/'+author)
    else:
        uf = UserForm()
    return render_to_response('../templates/userena/tra_add.html',{'uf':uf,'user':user})

#修改
from django.shortcuts import render_to_response,get_object_or_404
@csrf_exempt
def updatetra(request, travels_id):
    travels = get_object_or_404(Travels, pk=int(travels_id))
    if request.method == 'POST':
        uf = UserForm(request.POST, instance=travels)
        if uf.is_valid():
            title = uf.cleaned_data['title']
            content = uf.cleaned_data['content']
            contextinfo = uf.cleaned_data['contextinfo']
            image = uf.cleaned_data['image']
            bigimage = uf.cleaned_data['bigimage']
            city = uf.cleaned_data['city']
            author = request.user.username
            author_id = request.user.id
            travels.title = title
            travels.content = content
            travels.contextinfo = contextinfo
            travels.image = image
            travels.bigimage = bigimage
            travels.city = city
            travels.author = author
            travels.author_id = author_id
            travels.save()
            return HttpResponseRedirect('/list/'+author)
    return render_to_response('add.html',{'uf': UserForm(instance=travels)})

#删除
@csrf_exempt
def deletetra(request, travels_id):
    travels = get_object_or_404(Travels, pk=int(travels_id))

    travels.delete()
    author = request.user.username
    return HttpResponseRedirect('/list/'+author)
