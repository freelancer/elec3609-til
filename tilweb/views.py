from django.shortcuts import render
from django.http import HttpResponseNotAllowed, HttpResponseRedirect
from .models import Post
from .forms import TilForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


def index(request):
    if not request.user.is_authenticated:
        latest_posts = Post.objects.order_by('-post_date')[:5]
        return render(
            request, 'tilweb/index.html', {
                'posts': latest_posts
            })
    else:
        return HttpResponseRedirect('/post/')


def signup(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/post/')
    if request.method == 'GET':
        form = UserCreationForm()
        return render(request, 'tilweb/signup.html', {'form': form})
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/post/')
        else:
            return render(request, 'tilweb/signup.html', {'form': form})

def create_post(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect('/login/')
    elif request.method == 'GET':
        form = TilForm()
        latest_posts = Post.objects.filter(author=request.user).order_by('-post_date')[:5]
        return render(
            request, 'tilweb/create_post.html', {
                'form': form, 'posts': latest_posts
            })
    elif request.method == 'POST':
        form = TilForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            return HttpResponseRedirect('/post/1/')
    else:
        return HttpResponseNotAllowed('{0} Not allowed'.format(request.method))


def show_post(request, post_id=None):
    post = Post.objects.filter(id=post_id)[0]
    return render(request, 'tilweb/view_post.html', {
        'post': post,
    })
