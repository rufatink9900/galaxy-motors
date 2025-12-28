from django.urls import path
from . import views



urlpatterns = [
    path('', views.services, name='services'),
    path('<int:category_id>/', views.services, name='services_by_category'),
    path('<int:category_id>/<int:subcategory_id>/', views.services, name='services_by_subcategory'),
    path('service/<int:pk>/', views.service_detail, name='service_detail'),
]
