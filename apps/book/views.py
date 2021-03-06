from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import AuthorForm, BookForm

# Create your views here.

def Home(request):
    return render(request, 'index.html')

def createAuthor(request):
    if (request.method=='POST'):
        authorForm = AuthorForm(request.POST)
        if (authorForm.is_valid()):
            authorForm.save()
            return redirect('book:listAuthors')
    else:
        authorForm = AuthorForm()
    return render(request, 'bookApp/createAuthor.html', {'authorForm': authorForm})

def listAuthor(request):
    authors = Author.objects.all()
    return render(request, 'bookApp/listAuthors.html', {'authors': authors})

def visualizeAuthor(request, id):
    author = Author.objects.get(id=id)
    authorForm = AuthorForm()
    if (request.method=='GET'):
        authorForm = AuthorForm(instance=author)
    return render(request, 'bookApp/visualizeAuthor.html', {'authorForm':  authorForm})

def updateAuthor(request, id):
    author = Author.objects.get(id=id)
    authorForm = AuthorForm()
    if (request.method=='GET'):
        authorForm = AuthorForm(instance=author)
    else:
        authorForm = AuthorForm(request.POST, instance=author)
        if (authorForm.is_valid()):
            authorForm.save()
            return redirect('book:listAuthors')
    return render(request, 'bookApp/updateAuthor.html', {'authorForm': authorForm})

def deleteAuthor(request, id):
    author = Author.objects.get(id=id)
    authorForm = AuthorForm()
    if (request.method=='GET'):
        authorForm = AuthorForm(instance=author)
    else:
        author.delete()
        return redirect('book:listAuthors')
    return render(request, 'bookApp/deleteAuthor.html', {'authorForm': authorForm})

def createBook(request):
    if (request.method=='POST'):
        bookForm = BookForm(request.POST)
        if (bookForm.is_valid()):
            titleBook = bookForm.cleaned_data['titleBook']
            publicationDateBook = bookForm.cleaned_data['publicationDateBook']
            authorId = bookForm.cleaned_data['authorId']
            book = Book(titleBook=titleBook, publicationDateBook=publicationDateBook, authorId=authorId)
            book.save()
            return redirect('book:listBooks')
    else:
        bookForm = BookForm()
    return render(request, 'bookApp/createBook.html', {'bookForm': bookForm})

def listBook(request):
    books = Book.objects.all()
    return render(request, 'bookApp/listBooks.html', {'books': books})

def visualizeBook(request, id):
    book = Book.objects.get(id=id)
    if (request.method=='GET'):
        bookForm = BookForm(instance=book)
    return render(request, 'bookApp/visualizeBook.html', {'bookForm': bookForm})

def updateBook(request, id):
    book = Book.objects.get(id=id)
    if (request.method=='GET'):
        bookForm = BookForm(instance=book)
    else:
        bookForm = BookForm(request.POST, instance=book)
        if (bookForm.is_valid()):
            bookForm.save()
            return redirect('book:listBooks')
    return render(request, 'bookApp/updateBook.html', {'bookForm': bookForm})

def deleteBook(request, id):
    book = Book.objects.get(id=id)
    bookForm = BookForm()
    if (request.method=='GET'):
        bookForm = BookForm(instance=book)
    else:
        book.delete()
        return redirect('book:listBooks')
    return render(request, 'bookApp/deleteBook.html', {'bookForm': bookForm})