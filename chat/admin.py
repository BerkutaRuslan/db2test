from django.contrib import admin

# Register your models here.
from chat.models import Author, Messages

admin.site.register(Author)
admin.site.register(Messages)