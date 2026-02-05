from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('services/', include('services.urls')),
    path('applications/', include('apps.urls')),
    path('apps/', include('apps.urls')),
    path('accessories/', include('accessories.urls')),
    path('contact/', views.contact)
    # path('knowledge-base/', include('catalog.urls'))
]