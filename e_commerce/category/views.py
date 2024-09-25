from django.shortcuts import render
from .models import Category
from accounts.forms import  loginFrom
# Create your views here.
def category(req):
    form = loginFrom()
    categorys = Category.objects.all()
    return render(req,'category/index.html', {'categorys':categorys,'form': form})
