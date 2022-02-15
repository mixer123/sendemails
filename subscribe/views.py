from django.shortcuts import render
from sendemails.settings import EMAIL_HOST_USER
from . import forms
from .forms import *
from . models import *
from django.core.mail import send_mail

# Create your views here.
#DataFlair #Send Email
def subscribe(request):
    sub = forms.Subscribe()
    # form = Subscribe(request.POST)
    if request.method == 'POST':
        sub = forms.Subscribe.Email(request.POST)
        subject = 'Welcome to DataFlair'
        message = 'Hope you are enjoying your Django Tutorials'
        recepient = str(sub['Email'].value())
        send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently = False)
        email = Emails(address=forms.cleaned_data['address'])
        return render(request, 'success.html', {'recepient': recepient})
    return render(request, 'index.html', {'form':sub})