from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

class User(AbstractUser):
    CLASS_GRADES = [(str(i), f'{i} Grade') for i in range(1, 12)]
    class_grade = models.CharField(max_length=2, choices=CLASS_GRADES)
    groups = models.ManyToManyField(Group, related_name='books_user_set')
    user_permissions = models.ManyToManyField(Permission, related_name='books_user_set')

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField()
    published_date = models.DateField()
    cover_image = models.ImageField(upload_to='book_covers/', null=True, blank=True)
    pdf_file = models.FileField(upload_to='book_pdfs/', null=True, blank=True)
    class_grade = models.CharField(max_length=2, choices=User.CLASS_GRADES)
    is_trending = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user.username}: {self.content[:20]}'