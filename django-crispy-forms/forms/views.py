from django.shortcuts import render

from django.shortcuts import render
from django.views import generic

def init(request, *args, **kwargs):
  ctx = {}
  template = "index.html"

  return render(request, template, ctx)


from django.views.generic import CreateView
from forms.forms import AddressForm

class AddressView(CreateView):
    model = AddressForm
    fields = ('email', 'password', 'address_1', 'address_2', 'city', 'state', 'zip_code', 'check_me_out')
    template = "index.html"


class AddressFormView(generic.TemplateView):
  form_contact = AddressForm
  def get(self, request):
    context = {
      'form': self.form_contact,
    }
    return render(request, 'index.html', context)

class AddressFormView1(generic.TemplateView):
  form_contact = AddressForm
  def get(self, request):
    context = {
      'form': self.form_contact,
    }
    return render(request, 'index1.html', context)
