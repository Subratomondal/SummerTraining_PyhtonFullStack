from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from library.models import Book


# Create your views here.

# List all books
class BookListView(ListView):
    model = Book
    template_name = 'library/book_list.html'
    context_object_name = 'books'

# Show details of one book
class BookDetailView(DetailView):
    model = Book
    template_name = 'library/book_detail.html'
    context_object_name = 'book'

# Create a new book
class BookCreateView(CreateView):
    model = Book
    template_name = 'library/book_form.html'
    fields = ['title', 'author', 'published_year']
    success_url = reverse_lazy('book_list')


# Update an existing book
class BookUpdateView(UpdateView):
    model = Book
    template_name = 'library/book_form.html'
    fields = ['title', 'author', 'published_year']
    success_url = reverse_lazy('book_list')

# Delete a book
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'library/book_confirm_delete.html'
    success_url = reverse_lazy('book_list')




