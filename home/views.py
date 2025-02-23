
from .models import Review
from .forms import ReviewForm

from django.core.mail import send_mail

from django.contrib import messages
from .forms import PostForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Post
from django.contrib.auth.decorators import login_required

def post_list_view(request):
    posts = Post.objects.all()
    is_teacher = request.user.role == 'teacher'

    return render(request, 'home/post_list.html', {'posts': posts, 'is_teacher': is_teacher})


@login_required
def delete_post_view(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if post.author == request.user:
        post.delete()
    else:
        return redirect('post_list')

    return redirect('post_list')

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
                "Вітаємо! Ви успішно підписалися на оновлення платформи НМТ. Тепер ви будете першими, хто дізнається про новини та оновлення, що стосуються нашої платформи.\n\n"
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
