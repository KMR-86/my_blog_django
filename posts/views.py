from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Post


# Create your views here.
def post_home(request):
    return render(request, "post_home.html", {})


def post_create(request):
    return HttpResponse("<h1>Create</h1>")


def post_detail(request, id=None):  # retrieve
    instance = get_object_or_404(Post, id=id)
    context = {
        "function": "detail",
        "instance": instance,
    }
    return render(request, "post_detail.html", context)


def post_list(request):  # list items
    queryset = Post.objects.all();
    context = {
        "function": "list",
        "object": queryset
    }
    return render(request, "post_list.html", context)


def post_update(request):
    return HttpResponse("<h1>Update</h1>")


def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
