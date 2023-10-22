from django.shortcuts import render

from django.shortcuts import render

def init(request, *args, **kwargs):
  ctx = {}
  template = "base.html"

  return render(request, template, ctx)
