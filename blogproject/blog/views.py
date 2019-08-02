from django.shortcuts import render, redirect
from blog.models import Post
from django.contrib.auth import get_user_model
from django.http import HttpResponse

def index(request):
    posts = Post.objects.all().order_by('-created_date')
    context = {"posts": posts}
    return render(request, 'blog/index.html', context)

def detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {"post": post}
    return render(request, 'blog/detail.html', context)

def add(request):
    if request.method == 'POST':
        User = get_user_model()
        author = User.objects.get(username='zodlab')
        title = request.POST['title']
        content = request.POST['content']
        post = Post.objects.create(author=author, title=title, content=content)
        post_pk = post.pk
        return redirect('blog:detail', pk=post_pk)
    elif request.method == 'GET':
        return render(request, 'blog/add.html')

def delete(request, pk):
    if request.method == 'POST':
        post = Post.objects.get(pk=pk)
        post.delete()
        return render(request, 'blog/delete.html')
    elif request.method == 'GET':
        return HttpResponse('잘못된 접근입니다')