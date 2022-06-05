"""
Definition of urls for OUKwI_KS.
"""

from datetime import datetime
from django.urls import path, include
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from general import views as general_views
from Lab1 import views as lab1_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', general_views.home, name='home'),
    path('prescription/', lab1_views.prescriptionView.as_view(), name='prescription'),
    #path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    #path('login/',
    #     LoginView.as_view
    #     (
    #         template_name='app/login.html',
    #         authentication_form=forms.BootstrapAuthenticationForm,
    #         extra_context=
    #         {
    #             'title': 'Log in',
    #             'year' : datetime.now().year,
    #         }
    #     ),
    #     name='login'),
    #path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
    path('Lab2/', include('Lab2.urls',namespace='Lab2')),
    path('reset_password', auth_views.PasswordResetView.as_view(), name = 'set_password'),
    path('reset/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name = "password_reset_confirm"),
]

