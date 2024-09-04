from django.urls import path, include
from .views import (NewsListView,
                    NewsDetailView,
                    NewsCreateView,
                    NewsUpdateView,
                    NewsDeleteView,
                    PostViewSet)
from rest_framework import routers

notes_router = routers.SimpleRouter()
notes_router.register(
    r'notes',
    PostViewSet,
    basename='note',)

urlpatterns = [
    path('', NewsListView.as_view(), name='home'),
    path('post/<int:pk>/', NewsDetailView.as_view(), name='post_detail'),
    path('post/new/', NewsCreateView.as_view(), name='post_new' ),
    path('post/<int:pk>/edit/',NewsUpdateView.as_view(), name='post_edit'),
    path('post/<int:pk>/delete/', NewsDeleteView.as_view(), name='post_delete'),
    path('api/', include(notes_router.urls)),
]
