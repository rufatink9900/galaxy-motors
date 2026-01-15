from django.urls import path
from . import views

app_name = 'cars'

urlpatterns = [
    path('', views.catalog, name='knowledge_base'),  # Главная страница каталога
    path('<int:car_id>/', views.car_detail, name='car_detail'),  # Детальная страница
]