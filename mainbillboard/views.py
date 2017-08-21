from django.shortcuts import render
from django.utils import timezone
from mainbillboard.models import Messages
import json
from django.http import HttpResponse
from .forms import PostForm


# Create your views here.
def get_data(request):
    my_result = Messages.objects.order_by('-pub_date')
    for post in my_result:
        print(str(post))
    # posts is the key which contains a list of post objects
    return render(request, 'index.html', {"posts": my_result})


def add_post(request):
    my_result = Messages.objects.order_by('-pub_date')
    # when hitting the form submit button it automatically refreshes the page on
    # url of post/blog/ which sends a POST request, so lets check if form is valid
    if request.method == "POST":
        form = PostForm(request.POST)
        # If the form is valid
        if form.is_valid():
            post = form.save(commit=False)
            post.pub_date = timezone.now()
            post.save()
        return render(request, 'index.html', {"posts": my_result})
    # for form post request
    else:
        form = PostForm()
        return render(request, 'index-form.html', {'posts': my_result, 'form': form})