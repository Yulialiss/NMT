
from django.shortcuts import render, get_object_or_404, redirect
from .models import Test, Answer, TestResult, IncorrectAnswer

from django.utils.timezone import now, timedelta
from django.http import HttpResponse
from django.utils.dateparse import parse_datetime

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import TestResult, Subject

@login_required
def user_progress(request):
    user_results = {}
    test_results = TestResult.objects.filter(user=request.user).select_related('test__subject')

    for result in test_results:
        subject = result.test.subject
        if subject not in user_results:
            user_results[subject] = []
        user_results[subject].append(result)

    return render(request, 'testing/user_progress.html', {'user_results': user_results})

@login_required
def time_up(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    return render(request, 'testing/time_up.html', {'test': test})


@login_required
def test_detail(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = test.questions.all()

    if 'test_start_time' not in request.session:
        request.session['test_start_time'] = now().isoformat()

    if request.method == 'POST':
        test_end_time = now()
        test_start_time = parse_datetime(request.session.get('test_start_time'))
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

        test_result = TestResult.objects.create(user=request.user, test=test,score=score, max_score=questions.count(),time_spent=time_spent
        )

        for question in incorrect_answers:
            IncorrectAnswer.objects.create(user=request.user, question=question, test=test)

        if 'test_start_time' in request.session:
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

    for test in tests:
        last_result = TestResult.objects.filter(user=request.user, test=test).order_by('-date_taken').first()
        if last_result and last_result.max_score > 0:
            test.progress = round((last_result.score / last_result.max_score) * 100)
        else:
            test.progress = 0

    return render(request, 'testing/test_list.html', {'subject': subject, 'tests': tests})

@login_required
def test_result(request, result_id):
    result = get_object_or_404(TestResult, id=result_id)
    test = result.test
    questions = test.questions.all()
    user_answers = IncorrectAnswer.objects.filter(user=result.user, test=test).values_list('question', flat=True)

    return render(request, 'testing/test_result.html', {
        'result': result,
        'test': test,
        'questions': questions,
        'user_answers': user_answers,
        'formatted_time_spent': result.formatted_time_spent(),
    })


@login_required
def download_test_result(request, result_id):
    result = get_object_or_404(TestResult, id=result_id)
    test = result.test
    questions = test.questions.all()
    user_answers = IncorrectAnswer.objects.filter(user=result.user, test=test).values_list('question', flat=True)

    file_content = f"Результати тесту: {test.title}\n"
    file_content += f"Кількість правильних відповідей: {result.score} з {result.max_score}\n"
    file_content += f"Час проходження: {result.formatted_time_spent}\n\n"
    file_content += "Деталі відповідей:\n"

    for question in questions:
        if question.id in user_answers:
            status = "❌ Неправильна відповідь"
        else:
            status = "✅ Правильна відповідь"
        file_content += f"- {question.text} {status}\n"

    response = HttpResponse(file_content, content_type="text/plain")
    response['Content-Disposition'] = f'attachment; filename="test_result_{result.id}.txt"'
    return response


