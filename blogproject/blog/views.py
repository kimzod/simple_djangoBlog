from django.shortcuts import render
from blog.models import Post

def index(request):
    posts = Post.objects.filter(published_date__isnull=False).order_by('-created_date')
    context = {"posts": posts}
    return render(request, 'blog/index.html', context)

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {"post": post}
    return render(request, 'blog/detail.html', context)
