from django.shortcuts import render
from django.template import loader ,Context
from django.http import  HttpResponse
from blog.models import *
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import Http404
import time
from django.core.files.base import ContentFile

# Create your views here.
def archive(request):
    posts = BlogPost.objects.all()
    t = loader.get_template('blog.html')
    c = Context({'posts': posts})
    #return HttpResponse(t.render(c))
    return render_to_response('blog.html', {"posts": posts}, context_instance = RequestContext(request))


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





