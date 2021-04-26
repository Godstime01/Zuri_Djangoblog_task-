from django.views.generic import ListView, DetailView
# Create your views here.
from .models import Post

#home page view
class BlogListView(ListView):
    model = Post
    template_name='home.html'

# indivudual post view
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'