"""my_blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from posts.views import post_create
from posts.views import post_delete
from posts.views import post_detail
from posts.views import post_list
from posts.views import post_update
from posts.views import post_home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/', post_home),
    path("post/create",post_create),
    path("post/delete",post_delete),
    path("post/<int:id>/", post_detail, name="detail"),
    path("post/update", post_update),
    path("post/list", post_list)

]
