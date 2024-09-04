from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets

class NewsCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']

class NewsDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class NewsListView(ListView):
    model = Post
    template_name = 'home.html'
    # paginate_by = 3

class NewsUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']


class NewsDeleteView(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')

#######
class PostViewSet(viewsets.ModelViewSet):
    serializer_class=PostSerializer
    queryset = Post.objects.all()

class BaseViewSet(viewsets.ModelViewSet):
    def get_queryset(self):
        return self.model.objects.all()