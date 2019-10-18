from django.urls import path
from .views import *

app_name = "project"

urlpatterns = [
    path('', login, name='login'),
    path('register/', register, name='register'),
    path('add-project/', add_project, name='add-project'),
    path('edit-project/', edit_project, name='edit-project'),
    path('delete-project/', delete_project, name='delete-project'),
    path('filter-project/', filter_project, name='filter-project'),
    ]