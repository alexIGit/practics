from django.shortcuts import render

from blog.models import Post
# Create your views here.
def check(request):

  posts = Post.objects.prefetch_related('tags').select_related('author').all()

  print(posts)

  ctx = {}
  ctx['posts'] = posts
  template = 'index.html'
  return render(request, template, ctx)
