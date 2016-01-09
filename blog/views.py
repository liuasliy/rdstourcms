# -*- coding: UTF-8 -*-
from django.shortcuts import render
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from blog.models import *
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import Http404
import time
from django.core.files.base import ContentFile
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth

# Create your views here.
def archive(request):
    posts = BlogPost.objects.all()
    users = RdsUser.objects.all()
    t = loader.get_template('blog.html')
    c = Context({'posts': posts})
    #return HttpResponse(t.render(c))
    return render_to_response('blog.html', {"posts": posts, "users": users}, context_instance = RequestContext(request))


def detail(request, blog_id):
    try:
        posts = BlogPost.objects.get(id=blog_id)
    except BlogPost.DoesNotExist:
        raise Http404
    return render_to_response('blogdetails.html', {"posts": posts})



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
                return HttpResponseRedirect("/blog/")
            else:
                errors.append(u'登录失败，请重试')
    #response = render(request,'login.html',locals())
    response = render_to_response('login.html', {'errors': errors, },
        context_instance=RequestContext(request))
    return render(request, 'login.html', locals())

def logout(request):
    if request.user.is_authenticated():
        auth.logout(request)
        return render(request, "logout.html", {})
    else:
# return render(request,"logout.html",{})
        return HttpResponseRedirect("/blog/")



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






