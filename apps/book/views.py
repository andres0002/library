from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from .models import Author, Book
from .forms import AuthorForm, BookForm

# Create your views here.

class Home(TemplateView):
    template_name = 'index.html'

class CreateAuthor(CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'book/author/createAuthor.html'
    success_url = reverse_lazy('book:listAuthors')

class ListAuthor(ListView):
    model = Author
    template_name = 'book/author/listAuthors.html'
    context_object_name = 'authors'
    queryset = Author.objects.all()

class VisualizeAuthor(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'book/author/visualizeAuthor.html'
    success_url = reverse_lazy('book:listAuthors')

class UpdateAuthor(UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'book/author/updateAuthor.html'
    success_url = reverse_lazy('book:listAuthors')

class DeleteAuthor(DeleteView):
    model = Author
    success_url = reverse_lazy('book:listAuthors')

class CreateBook(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/book/createBook.html'
    success_url = reverse_lazy('book:listBooks')

class ListBook(ListView):
    model = Book
    template_name = 'book/book/listBooks.html'
    context_object_name = 'books'
    queryset = Book.objects.all()

class VisualizeBook(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book/book/visualizeBook.html'
    success_url = reverse_lazy('book:listBooks')

class UpdateBook(UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book/book/updateBook.html'
    success_url = reverse_lazy('book:listBooks')

class DeleteBook(DeleteView):
    model = Book
    success_url = reverse_lazy('book:listBooks')