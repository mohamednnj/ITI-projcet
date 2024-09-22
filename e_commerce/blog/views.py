from django.shortcuts import render
from .models import Blog

# Create your views here.
def blog(req):
    blogs = Blog.objects.all()
    return render(req,'blog/index.html',{'blogs':blogs} )