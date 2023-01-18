from django.contrib import admin
from authors.models import Author

# Register your models here.

@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'birthday_year')
    list_display_links = ('first_name', 'last_name', 'birthday_year')