from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Subject, Test, Question, Answer, TestResult, IncorrectAnswer
from .forms import TestForm

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
def test_detail(request, test_id):
    test = get_object_or_404(Test, id=test_id)
    questions = test.questions.all()

    if request.method == 'POST':
        form = TestForm(request.POST, test=test)
        if form.is_valid():
            score = 0
            incorrect_answers = []
            correct_answers = []

            for question in questions:
                answer_id = form.cleaned_data.get(f'question_{question.id}')
                answer = get_object_or_404(Answer, id=answer_id)

                if answer.is_correct:
                    score += 1
                    correct_answers.append(question)
                else:
                    incorrect_answers.append(question)
                    IncorrectAnswer.objects.create(user=request.user, question=question, test=test)

            test_result = TestResult.objects.create(
                user=request.user,
                test=test,
                score=score
            )
            return redirect('test_result', result_id=test_result.id)
    else:
        form = TestForm(test=test)

    return render(request, 'testing/test_detail.html', {'test': test, 'questions': questions, 'form': form})

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
    })
