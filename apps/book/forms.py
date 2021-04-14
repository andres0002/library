from django import forms
from apps.book.models import Author, Book

class AuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = [
                'nameAuthor',
                'lastNameAuthor',
                'nationalityAuthor',
                'descriptionAuthor'
        ]
        labels = {
                'nameAuthor': 'Name Author',
                'lastNameAuthor': 'Last Name Author',
                'nationalityAuthor': 'Nationality Author',
                'descriptionAuthor': 'Description Author'
        }
        widgets = {
            'nameAuthor': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Add Name Author'
                }
            ),
            'lastNameAuthor': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Add Last Name Author'
                }
            ),
            'nationalityAuthor': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Add Nationality Author'
                }
            ),
            'descriptionAuthor': forms.Textarea(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Add Description Author'
                }
            )
        }

class BookForm(forms.ModelForm):

    #def __init__(self, *args, **kwargs):
    #    super().__init__(*args, **kwargs)
    #    self.fields['authorId'].queryset = Author.objects.filter(statusAuthor=True)
    class Meta:
        model = Book
        fields = [
                'titleBook',
                'publicationDateBook',
                'authorId'
        ]
        labels = {
            'titleBook': 'Title Book',
            'publicationDateBook': 'Publication Date Book',
            'authorId': 'Authors'
        }
        widgets = {
            'titleBook': forms.TextInput(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Add Title Book'
                }
            ),
            'publicationDateBook': forms.SelectDateWidget(
                attrs = {
                    'class': 'form-control',
                    'placeholder': 'Add Publication Date Book'
                }
            ),
            'authorId': forms.SelectMultiple()
        }