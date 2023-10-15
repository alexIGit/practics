from django.urls import path
from .views import List

# app_name = 'orm_db'

urlpatterns = [
    # path('', views.form),
    path('', List.as_view(), name='orm_db'),
]