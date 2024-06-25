from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')), 
    path('login/', auth_views.LoginView.as_view(template_name='main/login.html'), name='login'),
    path('cart/', include('cart.urls')),
]
