from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, get_user_model, hashers, logout
from django.views import View
from django.contrib import messages


User = get_user_model()


class LoginView(View):
    template_name = 'login.html'
    contex = {}

    def get(self, request):
        return render(request, self.template_name, self.contex)

    def post(self, request):
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.error(request, "Username or password is not valid!")
                return redirect('/accounts/login')


class RegisterView(View):
    template_name = 'register.html'
    contex = {}

    def get(self, request):
        return render(request, 'register.html', self.contex)

    def post(self, request):
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            username = request.POST.get('username')
            password1 = request.POST.get('password1')
            password2 = request.POST.get('confirmation')

            if password1 == password2:
                if User.objects.filter(username=username).exists():
                    messages.error(request, "This username already exists")
                    return redirect('/accounts/sign-up')
                if User.objects.filter(email=email).exists():
                    messages.error(request, "This email already exists")
                    return redirect('/accounts/sign-up')
                else:
                    user = User.objects.create(
                        first_name=first_name,
                        last_name=last_name,
                        email=email,
                        username=username,
                        password=hashers.make_password(password2)
                    )
                    user.save()
                    return redirect('/accounts/login')
            else:
                messages.error(request, "Password are not the same")
                return redirect('/accounts/sign-up')


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('/')

