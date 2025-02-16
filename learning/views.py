from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Event
from .forms import EventForm
from django.shortcuts import render
from django.shortcuts import render


def calendar_view(request):
    events = Event.objects.all().order_by('date')
    return render(request, 'learning/index.html', {'events': events})

def add_event(request):
    if request.method == 'POST':
        import json
        data = json.loads(request.body)
        title = data.get('title')
        description = data.get('description')
        date = data.get('date')

        event = Event.objects.create(title=title, description=description, date=date)
        return JsonResponse({'success': True})
    return JsonResponse({'success': False}, status=400)

def learning_view(request):
    return render(request, 'learning/index.html')
