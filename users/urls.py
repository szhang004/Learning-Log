from django.urls import path
from . import views

from django.contrib.auth.views import LoginView

urlpatterns = [
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # 'login' arg sends request to Django's default login view so we don't include that view
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register, name='register'),
]