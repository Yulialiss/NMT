
from .models import Review
from .forms import ReviewForm
from django.contrib.auth.decorators import login_required

from django.shortcuts import render, redirect
from django.core.mail import send_mail

from django.contrib import messages


def subscribe(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            send_mail(
                "Підписка на платформу НМТ",
                "Шановний користувачу!\n\n"
                "Вітаємо! Ви успішно підписалися на оновлення платформи НМТ. Тепер ви будете першими, хто дізнається про новини та оновлення, що стосуються нашої платформи.\n\n"
                "Наша команда постійно працює над покращенням сервісу, щоб забезпечити вам найкращий досвід. Ми будемо надсилати вам важливу інформацію, а також цікаві матеріали для вашого розвитку.\n\n"
                "Якщо ви більше не хочете отримувати оновлення, ви завжди можете відписатися, натиснувши на посилання внизу цього листа.\n\n"
                "Дякуємо, що обрали нас! Ми раді мати вас серед наших користувачів.\n\n"
                "З найкращими побажаннями,\n"
                "Команда платформи НМТ",
                "yuliahuralgit@gmail.com",
                [email],
                fail_silently=False,
            )
            messages.success(request, "Ви успішно підписалися!")
    return redirect("home")


@login_required
def home(request):
    reviews = Review.objects.all().order_by('-created_at')
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            new_review = form.save(commit=False)
            new_review.user = request.user
            new_review.save()
            return redirect('home')
    else:
        form = ReviewForm()

    return render(request, 'home/index.html', {'form': form, 'reviews': reviews})

@login_required
def reviews_view(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()
            return redirect('reviews')
    else:
        form = ReviewForm()

    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'reviews.html', {'form': form, 'reviews': reviews})


def about_page(request):
    return render(request, 'home/about.html')
