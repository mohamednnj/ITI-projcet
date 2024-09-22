from django.shortcuts import render
from .models import Category
# Create your views here.
def category(req):
    categorys = Category.objects.all()
    return render(req,'category/index.html', {'categorys':categorys})