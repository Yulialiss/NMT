from django.shortcuts import render, get_object_or_404
from .models import Subject, Topic, Theory

def subject_list(request):
    subjects = Subject.objects.all()
    return render(request, 'theory/subject_list.html', {'subjects': subjects})


def topic_list(request, subject_id):
    subject = get_object_or_404(Subject, id=subject_id)

    topics = subject.topic_set.all()

    return render(request, 'theory/topic_list.html', {'subject': subject, 'topics': topics})

def theory_detail(request, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)

    theory = Theory.objects.filter(topic=topic).first()

    return render(request, 'theory/theory_detail.html', {'topic': topic, 'theory': theory})
