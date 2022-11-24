from django.urls import path

from django.views.decorators.csrf import csrf_exempt

from .list_view import ListView
from .register_view import RegisterView
from . import download_view

urlpatterns = [
    path('', download_view.DownloadView, name='download_view'),
    path('seminar/register', csrf_exempt(RegisterView.as_view()), name='register_view'),
    path('seminar/list', csrf_exempt(ListView.as_view()), name='list_view'),
]