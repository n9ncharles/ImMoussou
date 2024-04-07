
from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


def send_email(request):
    if request.method == 'POST':
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,  # Adresse e-mail expéditeur
            [email],  # Liste des destinataires (ici, l'utilisateur)
            fail_silently=False,
        )

        return HttpResponseRedirect(reverse('email_sent'))

    return render(request, '../templates/Html/contact.html')
