from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import Post
from .forms import PostForm

# Create your views here.
def post_home(request):
    return render(request, "post_home.html", {})


def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        print(form.cleaned_data.get("title"))
        instance.save()

    context = {
        "form": form,
    }
    return render(request, "post_form.html", context)


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


def post_update(request,id):
    instance = get_object_or_404(Post, id=id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "title": instance.title,
        "instance": instance,
        "form": form,
    }
    return render(request, "post_form.html", context)


def post_delete(request, id):
    instance = get_object_or_404(Post, id=id)
    instance.delete()
    return redirect("/post/list")

