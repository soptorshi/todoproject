from django.urls import path
from .views import add_task, delete_task, home, edit_task

urlpatterns = [
    path('',home, name = 'home'),
    path('taskadd/', add_task),
    path('taskdelete/<int:id>',delete_task),
    path('taskedit/<int:id>', edit_task),    
]