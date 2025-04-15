from django.shortcuts import render, redirect
from .forms import ProfileEditForm, UserEditForm
from .models import Profile
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from my_classes.models import Class

@login_required
def student_dashboard(request):
    user_classes = Class.objects.filter(students=request.user)
    return render(request, 'profile_app/student_dashboard.html', {'user_classes': user_classes})

@login_required
def profile_view(request):
    try:
        profile = request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    return render(request, 'profile_app/profile.html', {'user': request.user, 'profile': profile})

@login_required
def edit_profile(request):
    profile, created = Profile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
        else:
            return render(
                request,
                'profile_app/edit_profile.html',
                {
                    'user_form': user_form,
                    'profile_form': profile_form,
                    'errors': {
                        'user_form_errors': user_form.errors,
                        'profile_form_errors': profile_form.errors,
                    },
                    'profile': profile,
                }
            )
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=profile)
    return render(
        request,
        'profile_app/edit_profile.html',
        {'user_form': user_form, 'profile_form': profile_form, 'profile': profile}
    )
