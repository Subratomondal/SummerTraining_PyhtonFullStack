from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Patient

class PatientListView(ListView):
    model = Patient
    template_name = 'clinic/patient_list.html'
    context_object_name = 'patients'

class PatientDetailView(DetailView):
    model = Patient
    template_name = 'clinic/patient_detail.html'
    context_object_name = 'patient'

class PatientCreateView(CreateView):
    model = Patient
    template_name = 'clinic/patient_form.html'
    fields = ['name', 'age', 'contact', 'diagnosis', 'admission_date']
    success_url = reverse_lazy('patient_list')

class PatientUpdateView(UpdateView):
    model = Patient
    template_name = 'clinic/patient_form.html'
    fields = ['name', 'age', 'contact', 'diagnosis', 'admission_date']
    success_url = reverse_lazy('patient_list')

class PatientDeleteView(DeleteView):
    model = Patient
    template_name = 'clinic/patient_confirm_delete.html'
    success_url = reverse_lazy('patient_list')
