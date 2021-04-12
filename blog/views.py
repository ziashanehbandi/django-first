from django.shortcuts import render,get_object_or_404
from django.shortcuts import HttpResponse
from .models import Project,Blog


def project(request):
    project = Project.objects.all()
    return render(request,'djangoProject3/home.html',{'projects':project} )

def blog(request):
    blog = Blog.objects.all()
    return render(request,'blog/blog.html',{'blogs': blog})

def each_blog(request,blog_id):
    blog = get_object_or_404(Blog,pk=blog_id)
    return render(request, 'blog/eachBlog.html', {'blog':blog})
