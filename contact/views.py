from django.contrib import messages  # Додати
from .forms import ContactForm
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.conf import settings

def send_test_email(request):
    send_mail(
        'Тестовий лист',
        'Це тестовий лист від Django.',
        settings.EMAIL_HOST_USER,
        ['yuliahuralgit@gmail.com'],
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

            email_message = EmailMessage(
                subject=f"Повідомлення від {name}",
                body=message,
                from_email=settings.EMAIL_HOST_USER,
                to=['recipient@example.com'],
                reply_to=[email]
            )
            email_message.send(fail_silently=True)

            messages.success(request, 'Ваше повідомлення було успішно відправлено!')
            return redirect('contact')
        else:
            messages.error(request, 'Будь ласка, виправте помилки у формі.')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})
