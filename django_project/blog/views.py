from django.views.generic import ListView, DetailView
from .models import Post2


class BlogListView(ListView):
    model = Post2
    template_name = "home.html"


class BlogDetailView(DetailView):
    model = Post2
    template_name = "post_detail.html"
