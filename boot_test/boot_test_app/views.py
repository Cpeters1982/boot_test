from django.views.generic import CreateView, UpdateView, ListView 
from django.urls import reverse_lazy 
from boot_test_app.models import Person
from boot_test_app.forms import PersonForm


class PersonListView(ListView):
    model = Person
    context_object_name = 'boot_test_app'


class PersonCreateView(CreateView):
    model = Person
    fields = ('name', 'email', 'job_title', 'bio')
    success_url = reverse_lazy('person_list')

class PersonUpdateView(UpdateView):
    model  = Person
    form_class = PersonForm
    template_name = 'boot_test_app/person_update_form.html'
    success_url = reverse_lazy('person_list')