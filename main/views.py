from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import get_user_model
from django.db.models import Q

from .models import Todo
User = get_user_model()



class HomeView(View):
    template = 'index.html'
    context = {}

    def get(self, requets):
        product=Todo.objects.all()
        self.context.update({'message': product})
        return render(requets, self.template, self.context)


class AddTodoView(View):
    template = 'add_todo.html'
    contex = {}

    def get(self, request):
        return render(request, self.template, self.contex)

    def post(self, request):
        title = request.POST.get('message')
        user_id = request.user
        todos=Todo.objects.create(
            text=title,
            user=user_id
        )
        todos.save()
        return redirect('/')



class TodoView(View):
    template = 'todo.html'
    contex = {}

    def get(self, request):
        product=Todo.objects.all()
        self.contex.update({'todo': product})
        return render(request, self.template, self.contex)

    def post(self, request):
        id = request.POST.get('id')
        user = request.user
        shopping_cart =Todo.objects.filter(Q(pk__in=id) & Q(user=user))
        shopping_cart.delete()
        return redirect('/todo')
