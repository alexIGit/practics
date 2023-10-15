from django.shortcuts import render
from django.http import HttpResponse
from . import models
from . import forms
from django.views import generic
# Create your views here.


def test_view(request):
    # text = 'welcome to %s ' %request.path
    # host = 'host is %s ' %request.get_host()
    full_path = 'full path to %s ' %request.get_full_path()
    # secure = 'sequriti %s ' %request.is_secure()
    return HttpResponse(full_path)

def search_form(request):
    return render(request, 'search_form.html', {})

def search(request):
    text_empty = 'вы хотели найти пустую форму'
    

    if request.method == 'GET':
        if 'q' in request.GET:
            text_find = 'вы хотели найти %s' % request.GET['q']
            return HttpResponse(text_find)
        else:
            return HttpResponse(text_empty)

def file_input(request):
    name = request.POST['name']
    surname = request.POST['surname']
    birth = request.POST['birth']
    gender = request.POST['gender']

    some_file = open('some.txt', 'w')
    some_file.write("name: " + name + '\n')
    some_file.write("surname: " + surname + '\n')
    some_file.write("birth: " + birth + '\n')
    some_file.write("gender: " + gender + '\n')
    some_file.close()
    
    return HttpResponse("Данные успешно записаны")

# def form(request):
#     form_for_author1 = forms.AuthorOneForm
#     form_for_article = forms.ArticleForm
#     form_for_contact = forms.ContactForm

#     context = {
#         'form_for_author1': form_for_author1,
#         'form_for_article': form_for_article,
#         'form_for_contact': form_for_contact,
#     }

#     return render(request, 'form.html', context)

def add_author(request):
    form = forms.AuthorOneForm(request.POST)
    result = 'Автор успешно добавлен %s' % request.path

    if request.method == 'POST':
        if form.is_valid():
            data = form.cleaned_data
            form.save()
            print(data)
            return HttpResponse(result)


def add_article(request):
    form = forms.ArticleForm(request.POST)
    result = 'Статья добавлена %s' % request.path
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        form.save()
        print(data)
        return HttpResponse(result)


class ContactFormView(generic.TemplateView):
    form_for_author1 = forms.AuthorOneForm
    form_for_article = forms.ArticleForm
    form_contact = forms.ContactForm

    def post(self, request):
        form = forms.ContactForm(request.POST)

        context = {
            'form_for_author1': self.form_for_author1,
            'form_for_article': self.form_for_article,
            'form_contact': form,
        }

        if form.is_valid():
            data = form.cleaned_data
            return HttpResponse(data.items())
        else:
            return render(request, 'form.html', context)

    def get(self, request):
        context = {
            'form_for_author1': self.form_for_author1,
            'form_for_article': self.form_for_article,
            'form_contact': self.form_contact,
        }
        return render(request, 'form.html', context)

class UrlView(generic.TemplateView):
    form_submit_url = forms.UrlForm
 
    def get(self, request):
        context = {
            'form_url': self.form_submit_url
        }
        return render(request, 'url_form.html', context)

    def post(self, request):
        form = forms.UrlForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            print(data)
        else:
            print("form is invalid")
            context = {
                'form_url': form
            }
            return render(request, 'url_form.html', context)
        return HttpResponse(form.cleaned_data.items())
