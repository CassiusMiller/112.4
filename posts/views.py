from django.views.generic import(
  CreateView, 
  DetailView, 
  UpdateView, 
  DeleteView, 
  ListView
)

from .models import Post 
from django.urls import reverse_lazy

class PostUpdateView(UpdateView):
  template_name = "posts/edit.html"
  model = Post
  fields = [
    "title", "subtitle" , "body", "status"
  ]

class PostDeleteView(DeleteView):
  template_name = "posts/delete.html"
  model = Post
  success_url = reverse_lazy("list")