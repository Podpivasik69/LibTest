from django.urls import path
from .import views

urlpatterns = [
    path('', views.home_index, name='home_index'),
    path('list/', views.book_list, name='book_list'),
    path('book/<int:book_id>/', views.book_description, name='book_description'),
    path('book/add-book/', views.add_book, name='add_book'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
]
