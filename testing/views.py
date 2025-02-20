from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Subject, Test, Question, Answer, TestResult, IncorrectAnswer
from datetime import timedelta
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.timezone import now, timedelta
from .models import Test, Answer, IncorrectAnswer, TestResult
from .forms import TestForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Test, Answer, TestResult, IncorrectAnswer
from .forms import TestForm
from django.utils.timezone import now
from datetime import timedelta
from django.utils.timezone import now, timedelta

@login_required
def time_up(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    return render(request, 'testing/time_up.html', {'test': test})


@login_required
def test_detail(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = test.questions.all()
    last_result = TestResult.objects.filter(user=request.user, test=test).order_by('-date_taken').first()

    if last_result:
        last_taken_date = last_result.date_taken.date()
        today_date = now().date()
        if last_taken_date == today_date:
            return redirect('test_result', result_id=last_result.id)
    request.session['test_start_time'] = now().isoformat()

    if request.method == 'POST':
        test_end_time = now()
        test_start_time = now().fromisoformat(request.session['test_start_time'])
        time_spent = test_end_time - test_start_time

        score = 0
        incorrect_answers = []

        for question in questions:
            answer_id = request.POST.get(f'question_{question.id}')
            if answer_id:
                answer = get_object_or_404(Answer, id=answer_id)
                if answer.is_correct:
                    score += 1
                else:
                    incorrect_answers.append(question)

        test_result = TestResult.objects.create(
            user=request.user,
            test=test,
            score=score,
            max_score=questions.count(),
            time_spent=time_spent
        )

        for question in incorrect_answers:
            IncorrectAnswer.objects.create(user=request.user, question=question, test=test)

        del request.session['test_start_time']

        return redirect('test_result', result_id=test_result.id)

    return render(request, 'testing/test_detail.html', {
        'test': test,
        'questions': questions,
    })

@login_required
def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'testing/subject_list.html', {'subjects': subjects})

@login_required
def test_list(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)
    tests = subject.tests.all()
    return render(request, 'testing/test_list.html', {'subject': subject, 'tests': tests})

@login_required
def test_result(request, result_id):
    result = get_object_or_404(TestResult, id=result_id)
    test = result.test  # Отримуємо тест
    questions = test.questions.all()

    user_answers = IncorrectAnswer.objects.filter(user=result.user, test=test).values_list('question', flat=True)

    return render(request, 'testing/test_result.html', {
        'result': result,
        'test': test,
        'questions': questions,
        'user_answers': user_answers,
    })

