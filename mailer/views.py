from django.shortcuts import render
from .forms import EmailForm
from django.core.mail import send_mail
from django.conf import settings


def sendmail(request):
    messageSent = False
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            subject = "Testing if it's working ;)"
            message = cd['message']
            send_mail(subject, message,
                      settings.EMAIL_HOST_USER , [cd['recipient']],
                      fail_silently=False)
            messageSent = True
    else:
        form = EmailForm()
    return render(request, 'index.html', {
        'form': form,
        'messageSent': messageSent,})