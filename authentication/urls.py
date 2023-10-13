from django.urls import path, re_path

from .views import SignUpView, SignInView, UserView
from knox import views as knox_views

urlpatterns = [
    re_path('register/', SignUpView.as_view()),
    re_path('login/', SignInView.as_view()),
    re_path('user', UserView.as_view()),
    path('logout/', knox_views.LogoutView.as_view(), name="knox-logout"),
]
