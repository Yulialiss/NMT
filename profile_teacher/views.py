
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import TeacherProfileForm
from .models import TeacherProfile

@login_required
def teacher_profile_edit(request):
    if request.user.role != 'teacher':
        return redirect('profile')

    profile, created = TeacherProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        form = TeacherProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('teacher_profile')
    else:
        form = TeacherProfileForm(instance=profile)

    return render(request, 'profile_teacher/teacher_profile_edit.html', {'form': form})


@login_required
def teacher_profile_view(request):
    # Переконаємося, що доступ має лише користувач з роллю вчителя
    if request.user.role != 'teacher':
        return redirect('profile')
    # Отримуємо профіль вчителя або повертаємо None
    profile = getattr(request.user, 'teacher_profile', None)
    return render(request, 'profile_teacher/teacher_profile.html', {'profile': profile})
