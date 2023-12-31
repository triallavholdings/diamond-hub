"""core URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import include, path

urlpatterns = [
    path('', include('admin_gradient.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('edc_base.auth.urls')),
    path('admin/', include('edc_base.auth.urls')),
    path('edc_base/', include('edc_base.urls')),
    path('edc_protocol/', include('edc_protocol.urls')),
    path('edc_device/', include('edc_device.urls')),
]
