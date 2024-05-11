from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from events.models import Events
from events.forms import EventsModelForm

# Create your views here.


class EventsListView(ListView):
    model = Events
    template_name = 'events.html'
    context_object_name = 'events'

    def get_queryset(self):
        events = super().get_queryset().order_by('-id')
        search = self.request.GET.get('search')
        if search:
            events = events.filter(guests__icontains=search)

        return events


class NewEventView(CreateView):
    model = Events
    template_name = 'new_event.html'
    form_class = EventsModelForm
    success_url = '/events/'


class DetailEventView(DetailView):
    model = Events
    template_name = 'detail_event.html'
    context_object_name = 'event'


class UpdateEventView(UpdateView):
    model = Events
    template_name = 'update_event.html'
    form_class = EventsModelForm
    success_url = '/events/'


class DeleteEventView(DeleteView):
    model = Events
    template_name = 'delete_event.html'
    success_url = '/events/'
