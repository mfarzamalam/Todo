from django.urls import path, include
from .views import (
    read,
    create,
    update,
    delete,
)

app_name = 'crud'

urlpatterns = [
    path('',         read, name='read'),
    path('create/',  create, name='create'),
    path('update/',  update, name='update'),
    path('delete/',  delete, name='delete'),
]
