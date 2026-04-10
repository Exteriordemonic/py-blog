from django.shortcuts import render
from django.views.generic import ListView, DetailView
from blog.models import Post


# Create your views here.
class IndexView(ListView):
    model = Post
    template_name = "blog/index.html"
    context_object_name = "posts"
    paginate_by = 5


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
