from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Book, Message

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date', 'class_grade', 'is_trending')
    search_fields = ('title', 'author')
    list_filter = ('published_date', 'class_grade', 'is_trending')
    fields = ('title', 'author', 'description', 'published_date', 'cover_image', 'pdf_file', 'class_grade', 'is_trending')

admin.site.register(User, UserAdmin)
admin.site.register(Book, BookAdmin)
admin.site.register(Message)