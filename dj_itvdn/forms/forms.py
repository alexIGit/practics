from django.forms import ModelForm
from django.forms import Form

from . import models
from django import forms

from .models import Author1
from .models import Article

from django.http import HttpResponse
from django.core.validators import URLValidator, ValidationError

class AuthorOneForm(ModelForm):
    class Meta:
        model = Author1
        fields = ['name', 'surname', 'city']

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ['author', 'title', 'text']


class ContactForm(forms.Form):
    boolean_field = forms.BooleanField()
    float_field = forms.FloatField()
    name_sender = forms.CharField(max_length=100, label='Введите ваше имя')
    message = forms.CharField(widget=forms.Textarea, label='Cообщение')
    sender = forms.EmailField(label='Введите ваш email!')

class UrlForm(forms.Form):
    title = forms.CharField(label = "Название сайта")
    url = forms.CharField(label = "Адрес сайта")

    def clean(self):
        cleaned_data = super(UrlForm, self).clean()

    def clean_url(self):
        url = self.cleaned_data['url']
        validation_url = URLValidator()

        try:
            validation_url(url)
        except:
            raise forms.ValidationError("Это не адрес сайта!")
        return url