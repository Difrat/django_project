from django.views.generic import ListView
from .models import Post2


class BlogListView(ListView):
    model = Post2
    template_name = "home.html"
