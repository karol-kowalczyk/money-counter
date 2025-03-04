"""
URL configuration for da_money_counter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from backend_counter.api.views import ToPayAmountView, AlreadyPaidView
from backend_counter.check_day import PerformActionView
from django.conf.urls.static import static
from da_money_counter import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('payments/', ToPayAmountView.as_view(), name='to-pay'),
    path('payments/already-paid/', AlreadyPaidView.as_view(), name='paid'),
    path('check-date/', PerformActionView.as_view(), name='date'),
] + staticfiles_urlpatterns()
