# Generated by Django 3.1.7 on 2021-03-04 22:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_auto_20210304_1653'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['nameAuthor'], 'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
        migrations.AddField(
            model_name='author',
            name='createDateAuthor',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='author',
            name='updateDateAuthor',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titleBook', models.CharField(max_length=150)),
                ('publicationDateBook', models.DateTimeField()),
                ('createDateBook', models.DateTimeField(auto_now_add=True)),
                ('updateDateBook', models.DateTimeField(auto_now=True)),
                ('authorId', models.ManyToManyField(to='book.Author')),
            ],
            options={
                'verbose_name': 'Book',
                'verbose_name_plural': 'Books',
                'ordering': ['titleBook'],
            },
        ),
    ]
