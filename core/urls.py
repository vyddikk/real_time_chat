from django.contrib.auth import views as auth_views
from django.urls import path, reverse_lazy

from . import views
urlpatterns = [
    path('', views.frontpage, name='frontpage'),
    path('singup/', views.singup, name='singup'),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', views.my_logout, name='logout'),
]

