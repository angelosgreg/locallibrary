from django.urls import path
from . import views

urlpatterns = [
    path('catalog/', include('catalog.urls')),
]
