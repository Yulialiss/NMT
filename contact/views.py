
from .forms import ContactForm
from django.shortcuts import render, redirect

from django.core.mail import send_mail
from django.http import HttpResponse

def send_test_email(request):
    send_mail(
        'Тестовий лист',
        'Це тестовий лист від Django.',
        'yuliahuralgit@gmail.com',
        ['recipient@example.com'],
        fail_silently=False,
    )
    return HttpResponse('Тестовий лист відправлено!')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            send_mail(
                f"Повідомлення від {name}",
                message,
                email,
                ['recipient@example.com'],
                fail_silently=False,
            )
            return HttpResponse('Ваше повідомлення відправлено!')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})

