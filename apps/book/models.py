from django.db import models

# Create your models here.

class Author(models.Model):
    nameAuthor = models.CharField(max_length=150, blank=False, null=False)
    lastNameAuthor = models.CharField(max_length=150, blank=False, null=False)
    nationalityAuthor = models.CharField(max_length=100, blank=False, null=False)
    descriptionAuthor = models.TextField(blank=False, null=False)
    createDateAuthor = models.DateTimeField(auto_now_add=True)
    updateDateAuthor = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'
        ordering = ['nameAuthor']

    def __str__(self):
        return self.nameAuthor

class Book(models.Model):
    titleBook = models.CharField(max_length=150, blank=False, null=False)
    publicationDateBook = models.DateTimeField(blank=False, null=False)
    authorId = models.ManyToManyField(Author)
    createDateBook = models.DateTimeField(auto_now_add=True)
    updateDateBook = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Book'
        verbose_name_plural = 'Books'
        ordering = ['titleBook']

    def __str__(self):
        return self.titleBook

    def get_authorId(self):
        return ", ".join([str(c) for c in self.authorId.all()])