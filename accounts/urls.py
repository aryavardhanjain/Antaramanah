from django.urls import path
from . import views


urlpatterns = [
    path('registerUser/', views.registerUser, name='registerUser'),
    path('registerTherapist/', views.registerTherapist, name='registerTherapist'),

    path('login/', views.login, name='login'),
    path('loginTherapist/', views.loginTherapist, name='loginTherapist'),
    path('logout/', views.logout, name='logout'),
    path('myAccount/', views.myAccount, name='myAccount'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('therapistDashboard/', views.therapistDashboard, name='therapistDashboard'),
]