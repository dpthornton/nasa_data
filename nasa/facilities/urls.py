from django.urls import path, re_path, include
from django.contrib.auth import views as auth_views
from . import views
from .views import Facilities

app_name = 'facilities'

urlpatterns = [
    path('list', Facilities.as_view(), name='facilities'),
]