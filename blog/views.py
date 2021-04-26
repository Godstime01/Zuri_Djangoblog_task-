from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
# Create your views here.
from .models import Post
from django.urls import reverse_lazy

#home page view
class BlogListView(ListView):
    model = Post
    template_name='home.html'

# indivudual post view
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title','author', 'body']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields= ['title', 'body']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')