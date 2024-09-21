from django.shortcuts import render

# Create your views here.
def blog(req):
    return render(req,'blog/index.html', )