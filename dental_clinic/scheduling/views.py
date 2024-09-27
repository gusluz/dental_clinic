import calendar
from datetime import date, datetime, timedelta
from .models import Event
from django.http import JsonResponse
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, render


def calendario(request):
    return render(request, 'scheduling/calendar_events.html')



# def delete_event(request, event_id):
#     event = get_object_or_404(Event, id=event_id)
#     if request.method == 'POST':
#         event.delete()
#         return JsonResponse({'message': 'Event sucess delete.'})
#     else:
#         return JsonResponse({'message': 'Error!'}, status=400)

# def next_week(request, event_id):
#     event = get_object_or_404(Event, id=event_id)
#     if request.method == 'POST':
#         next = event
#         next.id = None
#         next.start_time += timedelta(days=7)
#         next.end_time += timedelta(days=7)
#         next.save()
#         return JsonResponse({'message': 'Sucess!'})
#     else:
#         return JsonResponse({'message': 'Error!'}, status=400)

# def next_day(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        next = event
        next.id = None
        next.start_time += timedelta(days=1)
        next.end_time += timedelta(days=1)
        next.save()
        return JsonResponse({'message': 'Sucess!'})
    else:
        return JsonResponse({'message': 'Error!'}, status=400)
