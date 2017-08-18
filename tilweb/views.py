from django.shortcuts import render
from .models import Post

# Create your views here.

from django.http import HttpResponse
def index(request):
    latest_posts = Post.objects.order_by('-post_date')[:5]
    output = '<br>'.join([p.subject for p in latest_posts])
    return HttpResponse(output)
