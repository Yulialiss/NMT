
from .forms import AssignmentForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Class, Assignment, AssignmentSubmission
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from .forms import AssignmentSubmissionForm
import os
from django.shortcuts import render, get_object_or_404
from .models import Class, Assignment

def assignment_list(request, class_id):
    school_class = get_object_or_404(Class, id=class_id)

    assignments = Assignment.objects.filter(school_class=school_class)

    return render(request, 'my_classes/assignment_list.html', {
        'school_class': school_class,
        'assignments': assignments
    })

@login_required
def view_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)

    attachment_name = None
    if assignment.attachment:
        attachment_name = os.path.basename(assignment.attachment.name)

    submissions = AssignmentSubmission.objects.filter(assignment=assignment)

    if request.method == 'POST':
        form = AssignmentSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.assignment = assignment
            submission.student = request.user
            submission.save()
            messages.success(request, 'Ви успішно здали завдання!')
            return redirect('assignment_list', class_id=assignment.school_class.id)
    else:
        form = AssignmentSubmissionForm()

    return render(request, 'my_classes/view_assignment.html', {
        'assignment': assignment,
        'form': form,
        'attachment_name': attachment_name,
        'submissions': submissions,
    })



@login_required
def class_detail(request, class_id):
    class_obj = get_object_or_404(Class, id=class_id)
    students = class_obj.students.all()

    assignments = Assignment.objects.filter(school_class=class_obj)

    if request.method == 'POST':
        if request.user != class_obj.author:
            messages.error(request, 'Ви не маєте прав для видалення учнів з цього класу.')
            return redirect('class_detail', class_id=class_obj.id)

        students_to_remove = request.POST.getlist('students_to_remove')
        for student_id in students_to_remove:
            student = class_obj.students.get(id=student_id)
            class_obj.students.remove(student)
            messages.success(request, f'Учень {student.username} був успішно видалений з класу.')

            if student == request.user:
                return redirect('my_classes')

        return redirect('class_detail', class_id=class_obj.id)

    return render(request, 'my_classes/class_detail.html', {
        'class': class_obj,
        'students': students,
        'assignments': assignments,
    })




@login_required
def add_assignment(request, class_id):
    school_class = get_object_or_404(Class, id=class_id, author=request.user)
    if request.method == 'POST':
        form = AssignmentForm(request.POST, request.FILES)
        if form.is_valid():
            assignment = form.save(commit=False)
            assignment.author = request.user
            assignment.school_class = school_class
            assignment.save()
            return redirect('assignment_list', class_id=class_id)
    else:
        form = AssignmentForm()
    return render(request, 'my_classes/add_assignment.html', {'form': form, 'class_id': class_id})

@login_required
def delete_class(request, class_id):
    class_obj = get_object_or_404(Class, id=class_id)

    if request.user != class_obj.author:
        messages.error(request, 'Ви не маєте прав для видалення цього класу.')
        return redirect('class_detail', class_id=class_obj.id)

    class_obj.delete()
    messages.success(request, 'Клас успішно видалений.')
    return redirect('my_classes')

@login_required
def join_class(request):
    if request.method == 'POST':
        code = request.POST.get('code')

        try:
            class_obj = Class.objects.get(password=code)
<<<<<<< HEAD
            if request.user not in class_obj.students.all():
                class_obj.students.add(request.user)
=======
            if request.user not in class_obj.students.all(): 
                class_obj.students.add(request.user)  
>>>>>>> 3b3db8d257dcd719d66ebc25d1b4ddaf6747f070
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
<<<<<<< HEAD
            new_class.generate_password()
=======
            new_class.generate_password()  

>>>>>>> 3b3db8d257dcd719d66ebc25d1b4ddaf6747f070
            new_class.save()
            return redirect('class_detail', class_id=new_class.id)
        else:
            return render(request, 'my_classes/my_classes.html', {'error': 'Назва класу обовʼязкова.'})

    return render(request, 'my_classes/my_classes.html')
@login_required
def my_classes(request):
    if request.user.role == 'teacher':
        classes = Class.objects.filter(author=request.user)
    else:
<<<<<<< HEAD
        classes = []
=======
        classes = [] 
>>>>>>> 3b3db8d257dcd719d66ebc25d1b4ddaf6747f070
    return render(request, 'my_classes/my_classes.html', {'classes': classes})

