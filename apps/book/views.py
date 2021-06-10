import json
from django.shortcuts import render, redirect
from django.core.serializers import serialize
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.http import HttpResponse, JsonResponse
from django.views.generic import TemplateView, ListView, UpdateView, CreateView, DeleteView, DetailView
from apps.book.models import Author, Book, Reservation
from apps.book.forms import AuthorForm, BookForm
from apps.user.mixins import UserPermissionRequiredMixin

# Create your views here.

#Lessons of authors.
class AuthorsList(LoginRequiredMixin, UserPermissionRequiredMixin, TemplateView):
    permission_required = ('user.view_author', 'user.add_author', 'user.change_author', 'user.delete_author')
    template_name = 'book/author/authors_table.html'

class AuthorsTable(LoginRequiredMixin, UserPermissionRequiredMixin, ListView):
    permission_required = ('user.view_author', 'user.add_author', 'user.change_author', 'user.delete_author')
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

class CreateAuthor(LoginRequiredMixin, UserPermissionRequiredMixin, CreateView):
    permission_required = 'user.add_author'
    model = Author
    form_class = AuthorForm
    template_name = 'book/author/create_author.html'

    def post(self, request, *args, **kwargs):
        if (request.is_ajax()):
            form = self.form_class(request.POST, request.FILES)
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

class UpdateAuthor(LoginRequiredMixin, UserPermissionRequiredMixin, UpdateView):
    permission_required = 'user.change_author'
    model = Author
    form_class = AuthorForm
    template_name = 'book/author/update_author.html'

    def post(self, request, *args, **kwargs):
        if (request.is_ajax()):
            form = self.form_class(request.POST, request.FILES, instance=self.get_object())
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

class DeleteAuthor(LoginRequiredMixin, UserPermissionRequiredMixin, DeleteView):
    permission_required = 'user.delete_author'
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

#Lessons of Books.
class BooksList(LoginRequiredMixin, UserPermissionRequiredMixin, TemplateView):
    permission_required = ('user.view_book', 'user.add_book', 'user.change_book', 'user.delete_book')
    template_name = 'book/book/books_table.html'

class BooksTable(LoginRequiredMixin, UserPermissionRequiredMixin, ListView):
    permission_required = ('user.view_book', 'user.add_book', 'user.change_book', 'user.delete_book')
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

class BooksReservationsList(LoginRequiredMixin, ListView):
    model = Reservation
    template_name = 'book/book/books_reservations_table.html'

    def get_queryset(self):
        return self.model.objects.filter(status=True, user=self.request.user)

class BooksReservationsTable(LoginRequiredMixin, ListView):
    model = Reservation

    def get_queryset(self):
        return self.model.objects.filter(status=True, user=self.request.user)

    def get_context_data(self, **kwargs):
        context = {}
        context['books_reservations'] = self.get_queryset()
        return context

    def get(self, request, *args, **kwargs):
        if (request.is_ajax()):
            return HttpResponse(serialize('json', self.get_queryset(), use_natural_foreign_keys=True), 'application/json')
        else:
            return redirect('book:books_reservations_list')

class CreateBook(LoginRequiredMixin, UserPermissionRequiredMixin, CreateView):
    permission_required = 'user.add_book'
    model = Book
    form_class = BookForm
    template_name = 'book/book/create_book.html'

    def post(self, request, *args, **kwargs):
        if (request.is_ajax()):
            form = self.form_class(request.POST, request.FILES)
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

class UpdateBook(LoginRequiredMixin, UserPermissionRequiredMixin, UpdateView):
    permission_required = 'user.change_book'
    model = Book
    form_class = BookForm
    template_name = 'book/book/update_book.html'

    def post(self, request, *args, **kwargs):
        if (request.is_ajax()):
            form = self.form_class(request.POST, request.FILES, instance=self.get_object())
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

class DeleteBook(LoginRequiredMixin, UserPermissionRequiredMixin, DeleteView):
    permission_required = 'user.delete_book'
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

class AvailableBooks(LoginRequiredMixin, ListView):
    model = Book
    paginate_by = 6
    template_name = 'book/book/available_books.html'

    def get_queryset(self):
        return self.model.objects.filter(amountBook__gte=1)

class AvailableBookDetail(LoginRequiredMixin, DetailView):
    model = Book
    template_name = 'book/book/available_book_detail.html'

    def get(self, request, *args, **kwargs):
        if (self.get_object().amountBook > 0):
            return render(request, self.template_name, {'object': self.get_object()})
        return redirect('book:available_books')

#Lessons of Reservations.
class ReservationRegister(LoginRequiredMixin, CreateView):
    model = Reservation
    success_url = reverse_lazy('book:available_books')

    def post(self, request, *args, **kwargs):
        if (request.is_ajax()):
            user = request.user
            book = Book.objects.filter(id = request.POST.get('book')).first()
            if (user and book):
                if (book.amountBook > 0):
                    new_reservation = self.model(
                        book = book,
                        user = user
                    )
                    new_reservation.save()
                    message = f'Successfully {self.model.__name__} registered.'
                    error = 'There are no errors.'
                    response = JsonResponse({'message':message, 'error':error, 'url': self.success_url})
                    response.status_code = 201
                    return response
        return redirect('book:available_books')

class ExpiredReservationsList(LoginRequiredMixin, TemplateView):
    template_name = 'book/book/expired_reservations_table.html'

class ExpiredReservationsTable(LoginRequiredMixin, ListView):
    model = Reservation

    def get_queryset(self):
        return self.model.objects.filter(status=False, user=self.request.user)

    def get_context_data(self, **kwargs):
        context = {}
        context['expired_reservations'] = self.get_queryset()
        return context

    def get(self, request, *args, **kwargs):
        if (request.is_ajax()):
            return HttpResponse(serialize('json', self.get_queryset(), use_natural_foreign_keys=True), 'application/json')
        else:
            return redirect('book:expired_reservations_list')