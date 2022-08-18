from logging import root
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index),
    path('progress/', views.progress)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

