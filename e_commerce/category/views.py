from django.shortcuts import render
from .models import Category
from accounts.forms import  loginForm
# Create your views here.
def category(req):
    form = loginForm()
    categorys = Category.objects.all()
    return render(req,'category/index.html', {'categorys':categorys,'formlogin': form})