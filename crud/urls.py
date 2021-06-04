from django.urls import path, include
from .views import (
    create_read,
    update,
    delete,
)

app_name = 'crud'

urlpatterns = [
    path('',                  create_read, name='create_read'),
    path('update/<int:pk>/',  update, name='update'),
    path('delete/<int:pk>/',  delete, name='delete'),
]
