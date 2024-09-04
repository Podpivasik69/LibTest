from django.urls import path
from django.contrib import admin
from .views import (
    ProviderListView,
    ProviderCreateView,
    ProviderUpdateView,
    ProviderDeleteView,
    ProviderDetailView,

    DeliveryListView,
    DeliveryCreateView,
    DeliveryUpdateView,
    DeliveryDeleteView,
    DeliveryDetailView,

)

urlpatterns = [
    path('', ProviderListView.as_view(), name='provider_list'),
    path('', DeliveryListView.as_view(), name='delivery_list'),
    # path('deliveries/', DeliveryListView.as_view(), name='deliveries'),
    path('', ProviderListView.as_view(), name='providers'),

    path('<int:pk>/', ProviderDetailView.as_view(), name='provider_detail'),
    path('new/', ProviderCreateView.as_view(), name='provider_new'),

    path('<int:pk>/update/', ProviderUpdateView.as_view(), name='provider_edit'),
    path('<int:pk>/delete/', ProviderDeleteView.as_view(), name='provider_delete'),



    path('deliveries/', DeliveryListView.as_view(), name='deliveries'), #+

    path('deliveries/<int:pk>/', DeliveryDetailView.as_view(), name='deliveries_detail'),
    path('deliveries/new/', DeliveryCreateView.as_view(), name='deliveries_new'),
    path('deliveries/<int:pk>/update/', DeliveryUpdateView.as_view(), name='deliveries_edit'),
    path('deliveries/<int:pk>/delete/', DeliveryDeleteView.as_view(), name='deliveries_delete'),
]