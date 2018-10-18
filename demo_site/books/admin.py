from django.contrib import admin
from .models import Book

# creating admin by running in shell
# python3 manage.py createsuperuser

# register Book table from .models
admin.site.register(Book)
