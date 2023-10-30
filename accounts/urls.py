from django.urls import path

from accounts.views import LoginView, RegisterView, LogoutView

urlpatterns = [
    path('login', LoginView.as_view(), name='sign_in'),
    path('sign-up', RegisterView.as_view(), name='sign_up'),
    path('logout', LogoutView.as_view(), name='logout')
]

