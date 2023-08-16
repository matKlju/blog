from django.shortcuts import render
from .forms import PostForm
from .models import Post

def PostList(request):
    posts = Post.objects.all()
    return render(request, 'blog/post_list.html', {'posts': posts})

def PostDetail(request, slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'blog/post_detail.html', {'post': post})

def PostCreate(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_create.html', {'form': form})

def PostEdit(request, slug):
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})