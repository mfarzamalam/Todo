from django.urls import path, include
from .views import (
    action,
    create,
    read,
    update,
    delete,
)

app_name = 'crud'

urlpatterns = [
    path('',                  action, name='action'),
    path('create/',           create, name='create'),
    path('read/',             read,   name='read'),
    path('update/<int:pk>/',  update, name='update'),
    path('delete/<int:pk>/',  delete, name='delete'),
]
