from django.urls import path

from . import views

urlpatterns = [
    path('register', views.RegisterFormView.as_view()),
    path('login', views.LoginFormView.as_view()),
    path('logout', views.LogoutView.as_view()),
    path('validate-email', views.validate_email),
    path('show-three', views.show_three),
    path('show-four', views.show_four),
    path('add-human', views.add_human),
    path('', views.MainView.as_view()),
]
