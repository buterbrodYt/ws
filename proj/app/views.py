from django.shortcuts import render
from .models import Book
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

# Create your views here.

class BookView(ListView):
    model = Book
    template_name = 'book.html'
    context_object_name = "books"

class BookCreateView(CreateView):
    model = Book
    fields = '__all__'
    template_name = 'bookCreate.html'
    success_url = reverse_lazy('main')

class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('main')
    template_name = 'bookDelete.html'

class BookUpdateView(UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'bookCreate.html'
    success_url = reverse_lazy('main')

class BookDetailView(DetailView):
    model = Book
    template_name = 'bookDetail.html'
    context_object_name = 'book'