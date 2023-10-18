from django.urls import path, include
from . import views
"""define URL para contas"""
app_name = 'accounts'
urlpatterns = [
    # inclui URLs de autenticaçao default
    path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register')
]
