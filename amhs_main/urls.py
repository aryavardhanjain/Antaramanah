"""
URL configuration for amhs_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/our_founders', views.our_founders, name='our_founders'),
    path('about/mission_vision', views.mission_vision, name='mission_vision'),
    path('contact', views.contact, name='contact'),
    path('faq', views.faq, name='faq'),
    path('services/children', views.services_children, name='services_children'),
    path('services/adolescents', views.services_adolescents, name='services_adolescents'),
    path('services/adults', views.services_adults, name='services_adults'),
    path('services/senior_citizens', views.services_senior_citizens, name='services_senior_citizens'),
    path('services/family', views.services_family, name='services_family'),
    path('services/couples', views.services_couples, name='services_couples'),
    path('services/consultation', views.services_psychiatric_consultation, name='services_psychiatric_consultation'),
    path('accounts/', include('accounts.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
