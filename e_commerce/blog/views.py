from django.shortcuts import render
from .models import Blog
from accounts.forms import SignupForm, loginFrom
# Create your views here.
def blog(req):
    blogs = Blog.objects.all()
    form = loginFrom()
    return render(req,'blog/index.html',{'blogs':blogs,'form': form} )