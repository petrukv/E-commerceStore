from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('product/<slug:slug>/', views.product_info, name='product-info'),
    path('search/<slug:category_slug>/', views.list_category, name='list-category'),

]
