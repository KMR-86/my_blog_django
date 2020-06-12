from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def post_home(request):
    return render(request,"post_home.html",{})


def post_create(request):
    return HttpResponse("<h1>Create</h1>")


def post_detail(request):  # retrieve
    context = {
        "function": "detail"
    }
    return render(request, "post_list.html", context)



def post_list(request):  # list items
    context={
        "function":"list"
    }
    return render(request,"post_list.html",context)


def post_update(request):
    return HttpResponse("<h1>Update</h1>")


def post_delete(request):
    return HttpResponse("<h1>Delete</h1>")
