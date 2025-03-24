
from .models import Review
from .forms import ReviewForm
from django.core.mail import send_mail
from django.contrib import messages
from .forms import PostForm
from django.shortcuts import render, redirect, get_object_or_404

from django.views.decorators.csrf import csrf_exempt
from .models import Post, Rating

import json
import base64
import hashlib
import uuid
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Review
from .forms import ReviewForm


@login_required
def reviews_view(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.save()

            response_data = {
                "success": True,
                "username": review.user.username,
                "content": review.content,
                "created_at": review.created_at.strftime("%Y-%m-%d %H:%M"),
                "photo": review.user.profile.photo.url if hasattr(review.user,
                                                                  "profile") and review.user.profile.photo else "https://i.pinimg.com/474x/36/52/05/365205dee1a12061c42a64d128ee4eb3.jpg"
            }
            return JsonResponse(response_data)
        else:
            return JsonResponse({"success": False, "errors": form.errors}, status=400)

    reviews = Review.objects.all().order_by('-created_at')
    return render(request, 'reviews.html', {'form': form, 'reviews': reviews})


PUBLIC_KEY = "sandbox_i82300391811"
PRIVATE_KEY = "sandbox_rvLPqs6QamwweYOPTlhsdJdBk9VlALicqJYNxn6b"
def generate_payment(request):
    unique_order_id = f"order_{uuid.uuid4().hex}"

    payment_data = {
        "version": "3",
        "public_key": PUBLIC_KEY,
        "action": "pay",
        "amount": "3000",
        "currency": "UAH",
        "description": "Оплата квитка",
        "order_id": unique_order_id,
        "result_url": "http://127.0.0.1:8000/pay/payment.html",
    }

    data_base64 = base64.b64encode(json.dumps(payment_data).encode()).decode()
    signature = base64.b64encode(hashlib.sha1(f"{PRIVATE_KEY}{data_base64}{PRIVATE_KEY}".encode()).digest()).decode()

    return JsonResponse({"data": data_base64, "signature": signature})
@csrf_exempt
@login_required
def rate_post(request, post_id):
    if request.method == "POST":
        post = Post.objects.get(id=post_id)
        score = int(request.POST.get("score"))

        rating, created = Rating.objects.update_or_create(
            user=request.user, post=post,
            defaults={"score": score}
        )

        post.update_rating()

        new_rating = round(post.rating, 1) if post.rating else 0.0

        return JsonResponse({
            "success": True,
            "new_rating": new_rating,
            "rating_count": post.rating_count
        })

    return JsonResponse({"success": False})

def post_list_view(request):
    posts = Post.objects.all()

    subject_filter = request.GET.get('subject', '')
    price_min = request.GET.get('price_min', '')
    price_max = request.GET.get('price_max', '')
    preparation_level_filter = request.GET.get('preparation_level', '')
    calendar_filter = request.GET.get('calendar', '')

    if subject_filter:
        posts = posts.filter(subjects__icontains=subject_filter)

    if price_min:
        posts = posts.filter(price_per_hour__gte=price_min)
    if price_max:
        posts = posts.filter(price_per_hour__lte=price_max)

    if preparation_level_filter:
        posts = posts.filter(preparation_levels__icontains=preparation_level_filter)

    if calendar_filter:
        posts = posts.filter(calendar__icontains=calendar_filter)

    is_teacher = request.user.is_authenticated and getattr(request.user, 'role', '') == 'teacher'

    return render(request, 'home/post_list.html', {
        'posts': posts,
        'is_teacher': is_teacher,
        'subject_filter': subject_filter,
        'price_min': price_min,
        'price_max': price_max,
        'preparation_level_filter': preparation_level_filter,
        'calendar_filter': calendar_filter
    })

@login_required
def delete_post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)

    if post.author == request.user:
        messages.warning(request, "Ви дійсно хочете видалити цей пост? Якщо так, повторіть дію.")
        post.delete()
        messages.success(request, "Пост успішно видалено.")
    else:
        messages.error(request, "Ви не можете видалити цей пост.")

    return redirect('post_list')

@login_required
def edit_post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author != request.user:
        messages.error(request, "Ви не можете редагувати цей пост.")
        return redirect('post_list')

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, "Пост успішно оновлено.")
            return redirect('post_list')
    else:
        form = PostForm(instance=post)

    return render(request, 'home/edit_post.html', {'form': form, 'post': post})

@login_required
def add_post_view(request):
    if request.user.role != 'teacher':
        return redirect('post_list')

    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_list')
    else:
        form = PostForm()

    return render(request, 'home/add_post.html', {'form': form})


def subscribe(request):
    if request.method == "POST":
        email = request.POST.get("email")
        if email:
            send_mail(
                "Підписка на платформу EdWay",
                "Шановний користувачу!\n\n"
                "Вітаємо! Ви успішно підписалися на оновлення платформи EdWAY. Тепер ви будете першими, хто дізнається про новини та оновлення, що стосуються нашої платформи.\n\n"
                "Наша команда постійно працює над покращенням сервісу, щоб забезпечити вам найкращий досвід. Ми будемо надсилати вам важливу інформацію, а також цікаві матеріали для вашого розвитку.\n\n"
                "Якщо ви більше не хочете отримувати оновлення, ви завжди можете відписатися, натиснувши на посилання внизу цього листа.\n\n"
                "Дякуємо, що обрали нас! Ми раді мати вас серед наших користувачів.\n\n"
                "З найкращими побажаннями,\n"
                "Команда платформи EdWay",
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





def about_page(request):
    return render(request, 'home/about.html')


def pay(request):
    return render(request, 'home/pay.html')


def payment_view(request):
    return render(request, 'home/payment.html')

def register(request):
    return render(request, "home/registration.html")
