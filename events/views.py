from django.shortcuts import redirect
from django.views import generic
from django.utils import timezone
from .models import Event, EventRegistration

class IndexView(generic.ListView):
    template_name = 'events/index.html'
    context_object_name = 'event_list'

    def get_queryset(self):
        return Event.objects.all()


class DetailView(generic.DetailView):
    model = Event
    template_name = 'events/detail.html'

def event_add_attendance(request, pk):
    try:
        this_event = Event.objects.get(pk=pk)
        if this_event.is_registration_active():
            this_event.add_user_to_list_of_attendees(user=request.user)
    except Exception as err:
        return redirect('events:detail', pk=pk)
    return redirect('events:detail', pk=pk)

def event_cancel_attendance(request, pk):
    try:
        this_event = Event.objects.get(pk=pk)
        if this_event.is_registration_active():
            this_event.remove_user_from_list_of_attendees(request.user)
    except Exception as err:
        return redirect('events:detail', pk=pk)
    return redirect('events:detail', pk=pk)

def event_add_transportation_attendance(request, pk):
    this_event = Event.objects.get(pk=pk)
    this_event.add_user_to_list_of_transportation(request.user)
    return redirect('events:detail', pk=pk)

def event_cancel_transportation_attendance(request, pk):
    this_event = Event.objects.get(pk=pk)
    this_event.remove_user_from_list_of_transportation(request.user)
    return redirect('events:detail', pk=pk)
