from django.shortcuts import render
from .models import Banner
from accounts.models import User
# Create your views here.
def home_page(req):
    banner = Banner.objects.all()
    return render(req,'homePage/index.html',{'banner':banner} )