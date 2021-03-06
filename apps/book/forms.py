from django import forms
from .models import Author, Book

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
                'nameAuthor',
                'lastNameAuthor',
                'nationalityAuthor',
                'descriptionAuthor'
        ]

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
                'titleBook',
                'publicationDateBook',
                'authorId'
        ]