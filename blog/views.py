from django.shortcuts import render
from .models import Post # >> the . before models means current directory/application <<
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(published__lte = timezone.now()).order_by('published')
    return render(request, 'blog/post_list.html', {'posts' : posts}) # >> takes request and calls function to render the template <<