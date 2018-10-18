from django.db import models


class Book(models.Model):



    def __str__(self):
        return self.name + '-' + self.author

    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    price = models.CharField(max_length=100)
    type = models.CharField(max_length=100)

# after making changes to the model structure, do migrations as follow
# 1. python3 manage.py makemigrations books (name of app) to register the changes to the structure
# 2. python3 manage.py sqlmigrate books 0001 to register the changes to be with the sql file
# 3. python3 manage.py migrate to commit the migrations

# adding items to database as follow
# 1. python3 manage.py shell
# 2. from books.models import Book
# 3.1 Book.objects.all() to list all items
# 3.2 a = Book()
# 3.3 a.name = 'Life' (etc.) -> a.save()