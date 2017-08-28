from django.shortcuts import render
from .models import Post
from .forms import TilForm
from django.urls import reverse


def index(request):
    form = TilForm()
    latest_posts = Post.objects.order_by('-post_date')[:5]
    return render(request, 'tilweb/create_post.html', {
                      'form': form, 'posts': latest_posts
                }
    )

def create_post(request):
    pass

def show_post(request):
    print(reverse('show-post'))
    post = Post.objects.filter(id=1)[0]
    return render(request, 'tilweb/view_post.html', {
        'post': post,
    })
