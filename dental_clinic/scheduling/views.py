import calendar
from datetime import date, datetime, timedelta
from .models import Event
from scheduling.forms import EventForm
from django.http import JsonResponse
from django.views import generic
from django.views.generic import ListView
from django.shortcuts import get_object_or_404, redirect, render


# def calendario(request):
#     return render(request, 'scheduling/calendar.html')

class CalendarView(generic.View):
    template_name = "scheduling/calendar.html"
    form_class = EventForm

    def get(self, request, *args, **kwargs):
        forms = self.form_class()
        events = Event.objects.get_all_events()
        events_month = Event.objects.get_running_events()
        event_list = []
        # start: '2020-09-16T16:00:00'
        for event in events:
            event_list.append(
                {   "id": event.id,
                    "title": event.patient_name,
                    "start": event.start_time.strftime("%Y-%m-%dT%H:%M:%S"),
                    "end": event.end_time.strftime("%Y-%m-%dT%H:%M:%S"),
                    "description": event.description,
                }
            )

        context = {"form": forms, "events": event_list,
                   "events_month": events_month}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        forms = self.form_class(request.POST)
        if forms.is_valid():
            form = forms.save(commit=False)
            form.save()
            return redirect("scheduling:calendar")
        context = {"form": forms}
        return render(request, self.template_name, context)


def delete_event(request, event_id):
    event = get_object_or_404(Event, id=event_id)
    if request.method == 'POST':
        event.delete()
        return JsonResponse({'message': 'Evento Deletado.'})
    else:
        return JsonResponse({'message': 'Error!'}, status=400)
    

def update_day(request, event_id):
    if request.method == 'POST':
        event_id = request.POST.get('id')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')

        event = get_object_or_404(Event, id=event_id)
        event.start_time = start_time
        event.end_time = end_time
        event.save()
        return JsonResponse({'message': 'Event updated successfully'})
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)
    

class RunningEventsListView(ListView):
    template_name = "scheduling/calendar.html"
    model = Event

    def get_queryset(self):
        return Event.objects.get_running_events()


