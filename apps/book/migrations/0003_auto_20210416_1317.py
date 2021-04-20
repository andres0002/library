# Generated by Django 3.1.7 on 2021-04-16 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20210416_1307'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='imageAuthor',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='book/authors/images/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='imageBook',
            field=models.ImageField(blank=True, max_length=255, null=True, upload_to='book/books/images/'),
        ),
    ]