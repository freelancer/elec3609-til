from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^me/', views.index, name='index'),
    url(r'^post/', views.show_post, name='show-post'),
]
