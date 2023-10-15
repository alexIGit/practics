from django.urls import path
from . import views
from . import forms

urlpatterns = [
    # path('', views.form),
    path('', views.ContactFormView.as_view()),
    path('url_form', views.UrlView.as_view()),

    path('test_view', views.test_view),
    path('search_form', views.search_form),
    path('search', views.search),
    path('file-input', views.file_input),
    path('add-author/', views.add_author),
    path('add-authorarticle/', views.add_article),
]