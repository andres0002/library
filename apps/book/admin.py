from django.contrib import admin
from .models import Author, Book

# Register your models here.

class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ('createDateAuthor', 'updateDateAuthor')
    list_display = ['nameAuthor', 'lastNameAuthor',
                    'nationalityAuthor', 'descriptionAuthor',
                    'createDateAuthor', 'updateDateAuthor'
                    ]
    list_filter = ('nationalityAuthor',)

class BookAdmin(admin.ModelAdmin):
    readonly_fields = ('createDateBook', 'updateDateBook')
    list_display = ['titleBook', 'publicationDateBook',
                    'get_authorId', 'createDateBook',
                    'updateDateBook'
                    ]
    list_filter = ('publicationDateBook',)

admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)