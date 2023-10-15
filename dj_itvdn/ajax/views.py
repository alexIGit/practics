from django.shortcuts import render

from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.http import JsonResponse

from .forms import UserCreateForm
from .forms import HumanForm

from orm_db.models import Human

import json

class MainView(TemplateView):
    template_name = 'ajax.html'
    human_form = HumanForm

    def get(self, request):
        # print(request)
        ctx = {}
        if request.user.is_authenticated:
            all_humans = Human.objects.all()
            ctx['humans'] = all_humans
            ctx['human_form'] = self.human_form
            return render(request, self.template_name, ctx)
        else:
            return render(request, self.template_name, {})

class RegisterFormView(FormView):
    # form_class = UserCreationForm
    form_class = UserCreateForm
    success_url = '/ajax/login/'
    template_name = 'register_ajax.html'

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

    def form_invalid(self, form):
        return super(RegisterFormView, self).form_invalid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = 'login_ajax.html'
    success_url = '/ajax'

    def form_valid(self, form):
        self.user = form.get_user()

        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/ajax/")


def validate_email(request):
    print(request)
    if request.GET:
        email = request.GET.get('email')
        is_taken = User.objects.filter(email=email).exists()

        if is_taken:
            data = {
                "is_taken": "Этот почтовый ящик уже занят"
            }
            return JsonResponse(data)
        else:
            return JsonResponse({
                'ok': "Этот почтовый ящик не занят)"
            })


def show_three(request):
    first_three = Human.objects.all()[:3].values()
    context = {
        'elements': list(first_three)
    }
    return JsonResponse(context)

def show_four(request):
    first_three = Human.objects.all()[:4].values()
    context = {
        'elements': list(first_three)
    }
    return JsonResponse(context)

@csrf_exempt
def add_human(request):
    print(request)
    if request.POST and request.is_ajax():
        print(request.POST)
        name = request.POST['name']
        surname = request.POST['surname']
        birth = request.POST['birth']
        company = request.POST['company']
        position = request.POST['position']
        language = request.POST['language']
        salary = request.POST['salary']

        human = Human.objects.create(name=name,
            surname=surname,
            birth=birth,
            company=company,
            position=position,
            language=language,
            salary=salary
        )

        return JsonResponse(human.dict())
