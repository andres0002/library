import json
from django.shortcuts import render, redirect
from django.core.serializers import serialize
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView
from apps.book.models import Author, Book
from apps.book.forms import AuthorForm, BookForm

# Create your views here.

class AuthorsList(LoginRequiredMixin, TemplateView):
    template_name = 'book/author/authors_table.html'

class AuthorsTable(LoginRequiredMixin, ListView):
    model = Author

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = {}
        context['authors'] = self.get_queryset()
        return context

    def get(self, request, *args, **kwargs):
        if (request.is_ajax()):
            return HttpResponse(serialize('json', self.get_queryset()), 'application/json')
        else:
            return redirect('book:authors_list')

class CreateAuthor(LoginRequiredMixin, CreateView):
    model = Author
    form_class = AuthorForm
    template_name = 'book/author/create_author.html'

    def post(self, request, *args, **kwargs):
        if (request.is_ajax()):
            form = self.form_class(request.POST)
            if (form.is_valid()):
                form.save()
                message = f'Successfully {self.model.__name__} registered.'
                error = 'There are no errors.'
                response = JsonResponse({'message':message, 'error':error})
                response.status_code = 201
                return response
            else:
                message = f'Errorful {self.model.__name__} register.'
                error = form.errors
                response = JsonResponse({'message':message, 'error':error})
                response.status_code = 400
                return response
        else:
            return redirect('book:authors_list')

class UpdateAuthor(LoginRequiredMixin, UpdateView):
    model = Author
    form_class = AuthorForm
    template_name = 'book/author/update_author.html'

    def post(self, request, *args, **kwargs):
        if (request.is_ajax()):
            form = self.form_class(request.POST, instance=self.get_object())
            if (form.is_valid()):
                form.save()
                message = f'Successfully {self.model.__name__} updation.'
                error = 'There are no errors.'
                response = JsonResponse({'message':message, 'error':error})
                response.status_code = 201
                return response
            else:
                message = f'Errorful {self.model.__name__} updation.'
                error = form.errors
                response = JsonResponse({'message':message, 'error':error})
                response.status_code = 400
                return response
        else:
            return redirect('book:authors_list')

class DeleteAuthor(LoginRequiredMixin, DeleteView):
    model = Author
    template_name = 'book/author/delete_author.html'

    def delete(self, request, *args, **kwargs):
        if (request.is_ajax()):
            author = self.get_object()
            author.delete()
            message = f'Successfully {self.model.__name__} elimination.'
            error = 'There are no errors.'
            response = JsonResponse({'message':message, 'error':error})
            response.status_code = 201
            return response
        else:
            redirect('book:authors_list')

class BooksList(LoginRequiredMixin, TemplateView):
    template_name = 'book/book/books_table.html'

class BooksTable(LoginRequiredMixin, ListView):
    model = Book

    def get_queryset(self):
        return self.model.objects.all()

    def get_context_data(self, **kwargs):
        context = {}
        context['books'] = self.get_queryset()
        return context

    def get(self, request, *args, **kwargs):
        if (request.is_ajax()):
            return HttpResponse(serialize('json', self.get_queryset(), use_natural_foreign_keys=True), 'application/json')
        else:
            return redirect('book:books_list')
class CreateBook(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book/book/create_book.html'

    def post(self, request, *args, **kwargs):
        if (request.is_ajax()):
            form = self.form_class(request.POST)
            if (form.is_valid()):
                form.save()
                message = f'Successfully {self.model.__name__} registered.'
                error = 'There are no errors.'
                response = JsonResponse({'message':message, 'error':error})
                response.status_code = 201
                return response
            else:
                message = f'Errorful {self.model.__name__} register.'
                error = form.errors
                response = JsonResponse({'message':message, 'error':error})
                response.status_code = 400
                return response
        else:
            return redirect('book:books_list')

class UpdateBook(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'book/book/update_book.html'

    def post(self, request, *args, **kwargs):
        if (request.is_ajax()):
            form = self.form_class(request.POST, instance=self.get_object())
            if (form.is_valid()):
                form.save()
                message = f'Successfully {self.model.__name__} updation.'
                error = 'There are no errors.'
                response = JsonResponse({'message':message, 'error':error})
                response.status_code = 201
                return response
            else:
                message = f'Errorful {self.model.__name__} updation.'
                error = form.errors
                response = JsonResponse({'message':message, 'error':error})
                response.status_code = 400
                return response
        else:
            return redirect('book:books_list')

class DeleteBook(LoginRequiredMixin, DeleteView):
    model = Book
    template_name = 'book/book/delete_book.html'

    def delete(self, request, *args, **kwargs):
        if (request.is_ajax()):
            book = self.get_object()
            book.delete()
            message = f'Successfully {self.model.__name__} elimination.'
            error = 'There are no errors.'
            response = JsonResponse({'message':message, 'error':error})
            response.status_code = 201
            return response
        else:
            return redirect('book:books_list')
