from django.shortcuts import render,redirect
from accounts.forms import  loginForm
from contact.forms import ContactForm
from django.http import HttpResponse
# Create your views here.
def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        formlogin = loginForm()
        form = ContactForm()
    return render(request, 'contact/index.html', {'formlogin': formlogin, 'form': form})
   

def success(request):
    return render(request, 'contact/success.html')