
from .forms import AssignmentForm

from django.http import HttpResponseForbidden
from .models import Class

from accounts.models import CustomUser
from django.contrib.auth.decorators import login_required
import os
from .forms import AssignmentSubmissionForm
from django.shortcuts import render, get_object_or_404, redirect

from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from .models import Assignment, AssignmentSubmission
from .forms import GradeFormSet


def grade_submissions(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    submissions = AssignmentSubmission.objects.filter(assignment=assignment)

    formset = GradeFormSet(queryset=submissions)

    if request.method == 'POST':
        formset = GradeFormSet(request.POST, queryset=submissions)
        if formset.is_valid():
            for form in formset:
                grade = form.cleaned_data.get('grade')
                if grade is not None:
                    form.instance.grade = grade
                    form.instance.save()
            messages.success(request, 'Оцінки успішно збережені!')
        else:
            messages.error(request, 'Виникли помилки при збереженні оцінок!')

    return render(request, 'my_classes/grade_submissions.html', {
        'assignment': assignment,
        'formset': formset,
    })


@login_required
def view_assignment(request, assignment_id):
    assignment = get_object_or_404(Assignment, id=assignment_id)

    attachment_name = None
    if assignment.attachment:
        attachment_name = os.path.basename(assignment.attachment.name)

    student_submission = AssignmentSubmission.objects.filter(
        assignment=assignment,
        student=request.user
    ).first()

    if request.method == 'POST':
        form = AssignmentSubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            if student_submission:
                student_submission.file_submission = form.cleaned_data['file_submission']
                student_submission.text_submission = form.cleaned_data['text_submission']
                student_submission.save()
                messages.success(request, 'Ваша робота оновлена!')
            else:
                submission = form.save(commit=False)
                submission.assignment = assignment
                submission.student = request.user
                submission.save()
                messages.success(request, 'Ви успішно здали завдання!')

            return redirect('view_assignment', assignment_id=assignment.id)
    else:
        form = AssignmentSubmissionForm()

    return render(request, 'my_classes/view_assignment.html', {
        'assignment': assignment,
        'form': form,
        'attachment_name': attachment_name,
        'student_submission': student_submission,
    })
@login_required
def delete_submission(request, submission_id):
    submission = get_object_or_404(AssignmentSubmission, id=submission_id, student=request.user)
    if request.method == 'POST':
        submission.delete()
        messages.success(request, 'Завдання видалено.')
    return redirect(request.META.get('HTTP_REFERER', 'home'))


@login_required
def class_members(request, class_id):
    class_instance = get_object_or_404(Class, id=class_id)

    if request.user != class_instance.author:
        messages.error(request, 'Ви не маєте прав для керування учнями в цьому класі.')
        return redirect('class_detail', class_id=class_instance.id)

    students = CustomUser.objects.filter(classes=class_instance)

    if request.method == 'POST':
        students_to_remove = request.POST.getlist('students_to_remove')
        for student_id in students_to_remove:
            student = CustomUser.objects.get(id=student_id)
            class_instance.students.remove(student)
            messages.success(request, f'Учень {student.username} був успішно видалений з класу.')

            if student == request.user:
                return redirect('my_classes')

        return redirect('class_members', class_id=class_instance.id)

    return render(request, 'my_classes/class_members.html', {'class': class_instance, 'students': students})


def assignment_list(request, class_id):
    school_class = get_object_or_404(Class, id=class_id)

    assignments = Assignment.objects.filter(school_class=school_class)

    return render(request, 'my_classes/assignment_list.html', {
        'school_class': school_class,
        'assignments': assignments
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
        'teacher_first_name': class_obj.teacher_first_name,
        'teacher_last_name': class_obj.teacher_last_name,
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

            if request.user not in class_obj.students.all():
                class_obj.students.add(request.user)

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
        section = request.POST.get('section') or ''
        subject = request.POST.get('subject')
        teacher_first_name = request.POST.get('first_name')
        teacher_last_name = request.POST.get('last_name')
        if class_name:
            new_class = Class(
                class_name=class_name,
                section=section,
                subject=subject,
                author=request.user,
                teacher_first_name=teacher_first_name,
                teacher_last_name=teacher_last_name
            )
            new_class.generate_password()
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

        classes = []

        classes = [] 

    return render(request, 'my_classes/my_classes.html', {'classes': classes})

