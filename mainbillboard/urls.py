from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.get_data, name='index'),
    # ex: /add_post
    url(r'^add_post', views.add_post, name='add_post'),
]