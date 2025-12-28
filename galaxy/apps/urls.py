from django.urls import path
from . import views


urlpatterns = [
    path('', views.apps_list, name='apps_list'),
    path('<int:pk>/', views.app_detail, name='app_detail'),
    path('<int:app_id>/download/', views.download_apk, name='download_apk'),
    path('q07/1.2.0/adb/set-language/', views.q07, name='q07_adb'),
]
