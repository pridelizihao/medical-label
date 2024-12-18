from django.contrib import admin
from django.urls import path
from .import views

app_name = "blog"

urlpatterns = [
    path("",views.index,name="index"),
    path("remendations",views.remendations,name="remendations"),
    path("team",views.team,name="team"),
    path("contact",views.contact,name="contact"),
    path("product",views.product,name="product"),
    path("blog/<int:blog_id>",views.blog_detail,name="blog_detail"),
    path("blog/pub",views.pub_blog,name="blog_pub"),
]