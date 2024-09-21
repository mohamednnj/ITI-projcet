from django.shortcuts import render

# Create your views here.
def category(req):
    return render(req,'category/index.html', )