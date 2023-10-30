from django.urls import path
from .views import HomeView, AddTodoView, TodoView

urlpatterns=[
    path('', HomeView.as_view(), name='home'),
    path('add-todo', AddTodoView.as_view(), name='todo'),
    path('todo', TodoView.as_view(), name='todohome')
]