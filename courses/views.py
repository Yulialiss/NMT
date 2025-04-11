
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import CourseForm

def edit_course(request, id):
    course = get_object_or_404(Course, id=id)

    if request.user != course.teacher:
        return redirect('courses')

    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', id=course.id)
    else:
        form = CourseForm(instance=course)

    return render(request, 'courses/edit_course.html', {'form': form, 'course': course})

def courses_page(request):
    if request.user.is_authenticated:
        if request.GET.get('my_courses') == 'true':
            courses = Course.objects.filter(teacher=request.user)
        else:
            courses = Course.objects.all()
    else:
        courses = Course.objects.all()

    return render(request, 'courses/courses.html', {'courses': courses})

def course_detail(request, id):
    course = get_object_or_404(Course, id=id)
    return render(request, 'courses/course_detail.html', {'course': course})

@login_required
def add_course(request):
    if request.user.role != 'teacher':
        return redirect('courses')

    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = form.save(commit=False)
            course.teacher = request.user
            course.save()
            return redirect('courses')
    else:
        form = CourseForm()

    return render(request, 'courses/add_course.html', {'form': form})

