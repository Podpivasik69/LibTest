from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_views

from auth_user import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('library/', include('library.urls')),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('', include('NewOrder.urls')),
    path('providers/', include('Delivery.urls')),

    # path('', include('Delivery_App.urls')),
    # path('api/', include('Delivery_App.urls')),
]

if settings.DEBUG:
 urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
