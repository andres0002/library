from django.urls import path
from .views import listAuthor, createAuthor, visualizeAuthor, updateAuthor, deleteAuthor
from .views import listBook, createBook, visualizeBook, updateBook, deleteBook

urlpatterns = [
    path('listAuthors/', listAuthor, name='listAuthors'),
    path('createAuthor/', createAuthor, name='createAuthor'),
    path('visualizeAuthor/<int:id>', visualizeAuthor, name='visualizeAuthor'),
    path('updateAuthor/<int:id>', updateAuthor, name='updateAuthor'),
    path('deleteAuthor/<int:id>', deleteAuthor, name='deleteAuthor'),
    path('listBooks/', listBook, name='listBooks'),
    path('createBook/', createBook, name='createBook'),
    path('visualizeBook/<int:id>', visualizeBook, name='visualizeBook'),
    path('updateBook/<int:id>', updateBook, name='updateBook'),
    path('deleteBook/<int:id>', deleteBook, name='deleteBook')
]