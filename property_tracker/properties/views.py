from django.shortcuts import render, get_object_or_404, redirect
from properties.models import Property
from properties.forms import PropertyForm
from django.urls import reverse_lazy
import json
from django.forms.models import model_to_dict
from django.http import JsonResponse
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView, ListView,
                                DetailView, CreateView,
                                UpdateView, DeleteView)
# Create your views here.

class AboutView(TemplateView):
    template_name ='about.html'

class PropertyListView(ListView):
    model = Property

    def get_queryset(self):
        return Property.objects.filter(published_date__lte=datetime.datetime.now()).order_by('-published_date')

class PropertyDetailView(DetailView):
    model = Property


class CreatePropertyView(LoginRequiredMixin,CreateView):
    login_url = '/login/'
    redirect_field_name = 'property/property_detail.html'
    form_class = PropertyForm
    model = Property

class PropertyUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'
    redirect_field_name = 'property/property_detail.html'
    form_class = PropertyForm
    model = Property

class PropertyDeleteView(LoginRequiredMixin,DeleteView):
    model = Property
    success_url = reverse_lazy('property_list')


class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'
    redirect_field_name = 'property/property_list.html'

    def get_queryset(self):
        return Property.objects.filter(published_date__isnull=True).order_by('create_date')


@login_required
def property_publish(request,pk):
    property = get_object_or_404(Property,pk=pk)
    property.publish()
    return redirect('property_detail',pk=pk)


def get_properties(request):
    queryset = Property.objects.values()
    return JsonResponse({"models_to_return": list(queryset)})
