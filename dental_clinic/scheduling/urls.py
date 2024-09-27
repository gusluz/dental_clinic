from django.urls import path
from . import views

app_name = "scheduling"

urlpatterns = [
    # path('calendar', views.calendario, name='calendario'),
    path('', views.CalendarView.as_view(), name='calendar'),
    path('delete_event/<int:event_id>', views.delete_event, name='delete_event'),
    path('update_day/<int:event_id>', views.update_day, name='update_day'),
]
