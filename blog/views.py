from django.shortcuts import render, get_object_or_404, redirect
from .models import Post # >> the . before models means current directory/application <<
from django.utils import timezone
from .forms import Post_Form


def post_list(request):
    posts = Post.objects.filter(published__lte = timezone.now()).order_by('published')
    return render(request, 'blog/post_list.html', {'posts' : posts}) # >> takes request and calls function to render the template <<

def post_detail(request, pk):
    Post.objects.get(pk=pk)

    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = Post_Form(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.published = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
        
    else:
        form = Post_Form()
    return render(request, 'blog/add_post.html', {'form': form})

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = Post_Form(request.POST, instance = post)
        if form.is_valid():
            post = form.save(commit = False)
            post.author = request.user
            post.published = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = Post_Form(instance=post)
    return render (request, 'blog/add_post.html', {'form': form})
