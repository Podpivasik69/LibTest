from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .models import Provider, Deliveries
from django.shortcuts import render

class ProviderCreateView(CreateView): #создание нового поставщика
    model = Provider
    template_name = 'Providers/provider_new.html'
    fields = ['name', 'agent_full_name', 'agent_phone']

class ProviderDetailView(DetailView):
    model = Provider
    template_name = 'Providers/provider_detail.html'


class ProviderListView(ListView): # список поставщиков
    model = Provider
    template_name = 'Providers/provider_list.html'
    paginate_by = 3

class ProviderUpdateView(UpdateView): # обновление поставщика
    model = Provider
    template_name = 'Providers/provider_edit.html'
    fields = ['name', 'agent_full_name', 'agent_phone']

class ProviderDeleteView(DeleteView):  #  удаление поставщика
    model = Provider
    template_name = 'Providers/provider_delete.html'
    success_url = reverse_lazy('provider_list')


##########################################################################################

class DeliveryCreateView(CreateView):
    model = Deliveries
    template_name = 'Deliveries/delivery_new.html'
    fields = ['delivery_number', 'delivery_data', 'provider', 'delivery_item', 'delivery_price', 'delivery_count']

class DeliveryDetailView(DetailView):
    model = Deliveries
    template_name = 'Deliveries/delivery_detail.html'

class DeliveryListView(ListView):
    model = Deliveries
    template_name = 'Deliveries/delivery_list.html'
    paginate_by = 3


class DeliveryUpdateView(UpdateView):
    model = Deliveries
    template_name = 'Deliveries/delivery_edit.html'
    fields = ['delivery_number', 'delivery_data','provider', 'delivery_item', 'delivery_price', 'delivery_count']


class DeliveryDeleteView(DeleteView):
    model = Deliveries
    template_name = 'Deliveries/delivery_delete.html'
    success_url = reverse_lazy('delivery_list')



















