from django.urls import path
from . import views
urlpatterns = [
    path('', views.accessories, name="accessories"),
    path("<int:pk>/", views.accessory_detail, name="accessory_detail"),
]
