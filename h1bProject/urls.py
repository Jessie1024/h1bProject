"""h1bProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('h1b/display/',views.h1b_display),
    path('h1b_home/',views.h1b_home),
    path('h1b_list/',views.h1b_list),
    path('h1b_list_more/',views.h1b_list_more),
    path('get_company/',views.get_company),
    path('get_naics_company/',views.get_naics_company),
    path('get_selected_naics/',views.get_selected_naics),
    path('h1b/chart/',views.sponor_chart_data),
    path('h1b_industry/',views.h1b_industry),
    path('h1b/industry/chart/',views.h1b_industry_chart),
    path('get_selected_companyID/',views.get_selected_companyID),
    path('get_selected_companyID_more/',views.get_selected_companyID_more),
    path('h1b_occupation/',views.h1b_occupation),
    path('h1b/occuption/chart/',views.h1b_occuption_chart),
    path('get_soc_company/',views.get_soc_company),
    path('get_selected_soc/',views.get_selected_soc),
    path('index/',views.h1b_index),
    path('index_occupation/',views.index_occupation),
    path('index_industry/', views.index_industry),
    path('index_sponsor/', views.index_sponsor),
    path('index_sponsor_more/', views.index_sponsor_more),
    path('contact/', views.contact),
    path('dir1/', views.dir1),
    path('dir2/', views.dir2),
    path('dir3/', views.dir3),
]
