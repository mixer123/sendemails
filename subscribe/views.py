from django.shortcuts import render, redirect
from sendemails.settings import EMAIL_HOST_USER

from .forms import *
from .models import *
from django.core.mail import send_mail


# Create your views here.
# DataFlair #Send Email
def subscribe(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            subject = 'Welcome to DataFlair'
            message = 'Hope you are enjoying your Django Tutorials'
            recepient = str(form['address'].value())

            send_mail(subject, message, EMAIL_HOST_USER, [recepient], fail_silently=False)
            email = Emails(address=form.cleaned_data['address'])
            email.save()
            return render(request, 'success.html', {'recepient': recepient})
    else:
        form = EventForm()  # A empty, unbound form

        return render(request, 'index.html', {'form': form})


def emailmass(request):
    allemails = Emails.objects.all()
    if request.method == 'POST':
        form = EmailMassForm(request.POST)
        if form.is_valid():
            subject = 'Masówka emaili'
            message = str(form['text'].value())
            for email in allemails:
                send_mail(subject, message, EMAIL_HOST_USER, [email.address], fail_silently=False)
            return redirect('/emailmass/')
    else:
        form = EmailMassForm()

        return render(request, 'emailmass.html', {'form': form})
