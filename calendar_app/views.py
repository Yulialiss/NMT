from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
import json
from .models import Event

@login_required
def calendar_view(request):
    return render(request, 'calendar_app/calendar.html')

@csrf_exempt  # Для тестування (небезпечно в продакшені)
@login_required
def add_event(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            event = Event.objects.create(
                user=request.user,
                title=data["title"],
                description=data.get("description", ""),
                date=data["date"]
            )
            return JsonResponse({
                "id": event.id,
                "title": event.title,
                "description": event.description,
                "date": str(event.date)
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=400)

@login_required
def get_events(request):
    events = Event.objects.filter(user=request.user).values("id", "title", "description", "date")
    return JsonResponse(list(events), safe=False)
