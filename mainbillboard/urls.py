from django.conf.urls import url
from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.get_data),
    # ex: /polls/5/
    url(r'^addpost', views.add_post),
]