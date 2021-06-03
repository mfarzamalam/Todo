from django.urls import path, include
from .views import (
    home_page
)

app_name = 'base'

urlpatterns = [
    path('', home_page, name='home'),
]