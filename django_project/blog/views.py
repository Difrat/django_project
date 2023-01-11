from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Post2


class BlogListView(ListView):
    model = Post2
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post2
    template_name = "post_detail.html"


class BlogCreateView(CreateView):
    model = Post2
    template_name = "post_new.html"
    fields = ["title", "author", "body"]


class BlogUpdateView(UpdateView):
    model = Post2
    template_name = "post_edit.html"
    fields = ["title", "body"]


class BlogDeleteView(DetailView):
    model = Post2
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")

