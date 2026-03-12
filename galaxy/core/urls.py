from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('services/', include('services.urls')),
    path('apps/', views.apps, name="apps"),
    # path('accessories/', include('accessories.urls')),
    path('contact/', views.contact, name="contact"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('server/', views.server, name='server'),
    path('links/', views.links, name="links")
    # path('knowledge-base/', include('catalog.urls'))
]