from django.shortcuts import render, redirect, get_object_or_404
from .models import Class
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Class, StudentClass
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Class, StudentClass
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Class


@login_required
def join_class(request):
    if request.method == 'POST':
        code = request.POST.get('code')

        try:
            class_obj = Class.objects.get(password=code)
            if request.user not in class_obj.students.all(): 
                class_obj.students.add(request.user)  
                messages.success(request, f'Ви приєдналися до класу "{class_obj.class_name}".')
            else:
                messages.info(request, 'Ви вже приєдналися до цього класу.')

            return redirect('class_detail', class_id=class_obj.id)
        except Class.DoesNotExist:
            messages.error(request, 'Невірний код курсу. Спробуйте ще раз.')

    return render(request, 'my_classes/join_class.html')


@login_required
def create_class(request):
    if request.user.role != 'teacher':
        return HttpResponseForbidden("Лише вчителі можуть створювати класи.")
    if request.method == 'POST':
        class_name = request.POST.get('class_name')
        section = request.POST.get('section')
        subject = request.POST.get('subject')
        audience = request.POST.get('audience')
        if class_name:
            new_class = Class(
                class_name=class_name,
                section=section,
                subject=subject,
                audience=audience,
                author=request.user
            )
            new_class.generate_password()  

            new_class.save()
            return redirect('my_classes')
        else:
            return render(request, 'my_classes/my_classes.html', {'error': 'Назва класу обовʼязкова.'})

    return render(request, 'my_classes/my_classes.html')


@login_required
def class_detail(request, class_id):
    class_obj = get_object_or_404(Class, id=class_id)
    return render(request, 'my_classes/class_detail.html', {'class': class_obj})


@login_required
def my_classes(request):
    if request.user.role == 'teacher':
        classes = Class.objects.filter(author=request.user)
    else:
        classes = [] 
    return render(request, 'my_classes/my_classes.html', {'classes': classes})

