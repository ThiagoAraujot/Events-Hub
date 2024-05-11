from django.contrib import admin
from django.urls import path
from events.views import EventsListView, NewEventView, DeleteEventView, DetailEventView, UpdateEventView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('events/', EventsListView.as_view(), name='events'),
    path('new-event/', NewEventView.as_view(), name='new-event'),
    path('event/<int:pk>', DetailEventView.as_view(), name='detail-event'),
    path('event/<int:pk>/delete', DeleteEventView.as_view(), name='delete-event'),
    path('event/<int:pk>/update', UpdateEventView.as_view(), name='update-event'),
]
