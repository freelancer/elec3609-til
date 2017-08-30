from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^me/', views.index, name='index'),
    url(r'^post/$', views.create_post, name='create-post'),
    url(r'^post/(?P<post_id>\d+)/$', views.show_post, name='show-post'),
    url(r'^signup/$', views.signup, name='signup'),

]
