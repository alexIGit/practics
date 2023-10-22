from django.urls import path
from forms import views

urlpatterns = [
  path('', views.init),
  path('0/', views.AddressFormView.as_view()),
  path('1/', views.AddressFormView1.as_view()),
]
