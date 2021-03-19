from django.urls import path
from django.contrib.auth.decorators import login_required
from .views import ListAuthor, CreateAuthor, VisualizeAuthor, UpdateAuthor, DeleteAuthor
from .views import ListBook, CreateBook, VisualizeBook, UpdateBook, DeleteBook

urlpatterns = [
    path('listAuthors/', login_required(ListAuthor.as_view()), name='listAuthors'),
    path('createAuthor/', login_required(CreateAuthor.as_view()), name='createAuthor'),
    path('visualizeAuthor/<int:pk>', login_required(VisualizeAuthor.as_view()), name='visualizeAuthor'),
    path('updateAuthor/<int:pk>', login_required(UpdateAuthor.as_view()), name='updateAuthor'),
    path('deleteAuthor/<int:pk>', login_required(DeleteAuthor.as_view()), name='deleteAuthor'),
    path('listBooks/', login_required(ListBook.as_view()), name='listBooks'),
    path('createBook/', login_required(CreateBook.as_view()), name='createBook'),
    path('visualizeBook/<int:pk>', login_required(VisualizeBook.as_view()), name='visualizeBook'),
    path('updateBook/<int:pk>', login_required(UpdateBook.as_view()), name='updateBook'),
    path('deleteBook/<int:pk>', login_required(DeleteBook.as_view()), name='deleteBook')
]