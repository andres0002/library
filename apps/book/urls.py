from django.urls import path
from apps.book.views import *

urlpatterns = [
    #Author views.
    path('authors_list/', AuthorsList.as_view(), name='authors_list'),
    path('authors_table/', AuthorsTable.as_view(), name='authors_table'),
    path('create_author/', CreateAuthor.as_view(), name='create_author'),
    path('update_author/<int:pk>/', UpdateAuthor.as_view(), name='update_author'),
    path('delete_author/<int:pk>/', DeleteAuthor.as_view(), name='delete_author'),
    #Book views.
    path('books_list/', BooksList.as_view(), name='books_list'),
    path('books_table/', BooksTable.as_view(), name='books_table'),
    path('create_book/', CreateBook.as_view(), name='create_book'),
    path('update_book/<int:pk>/', UpdateBook.as_view(), name='update_book'),
    path('delete_book/<int:pk>/', DeleteBook.as_view(), name='delete_book'),
    #General views.
    path('available-books/', AvailableBooks.as_view(), name='available_books'),
    path('books-reservations-list/', BooksReservationsList.as_view(), name='books_reservations_list'),
    path('expired-reservations-list/', ExpiredReservationsList.as_view(), name='expired_reservations_list'),
    path('books-reservations-table/', BooksReservationsTable.as_view(), name='books_reservations_table'),
    path('expired-reservations-table/', ExpiredReservationsTable.as_view(), name='expired_reservations_table'),
    path('available-book-detail/<int:pk>/', AvailableBookDetail.as_view(), name='available_book_detail'),
    path('book-reservation/', ReservationRegister.as_view(), name='book_reservation')
]