"""Django_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path
from telemetryhub.views import telemetry_hub, search_id


app_name = 'telemetryhub'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('telemetry_hub/', telemetry_hub),
    path('telemetry_hub/<str:farm_job_id>', telemetry_hub),
    path('telemetry_hub/<str:farm_job_id>/', telemetry_hub),
    path('telemetry_hub/<str:farm_job_id>/<str:service>',
         telemetry_hub),
    path('telemetry_hub/<str:farm_job_id>/<str:service>/',
         telemetry_hub),
    path('telemetry_hub/<str:farm_job_id>/<str:service>/<str:env_type>',
         telemetry_hub),
    path('telemetry_hub/<str:farm_job_id>/<str:service>/<str:env_type>/',
         telemetry_hub),
    path('telemetry_hub/<str:farm_job_id>/<str:service>/<str:env_type>/'
         '<int:family>', telemetry_hub),
    path('telemetry_hub/<str:farm_job_id>/<str:service>/<str:env_type>/'
         '<int:family>/', telemetry_hub),
    path('telemetry_hub/<str:farm_job_id>/<str:service>/<str:env_type>/'
         '<int:family>/<str:test_case>', telemetry_hub),
    path('telemetry_hub/<str:farm_job_id>/<str:service>/<str:env_type>/'
         '<int:family>/<str:test_case>/', telemetry_hub),
    path('telemetry_hub/<str:farm_job_id>/<str:service>/<str:env_type>/'
         '<int:family>/<str:test_case>/<str:json_type>', telemetry_hub),
    path('search_id/', search_id),
]
