from django.test import TestCase
from .models import Book

class BookModelTest(TestCase):

    def setUp(self):
        Book.objects.create(title="Test Book", author="Test Author", description="Test Description")

    def test_book_content(self):
        book = Book.objects.get(id=1)
        expected_object_name = f'{book.title} by {book.author}'
        self.assertEqual(expected_object_name, 'Test Book by Test Author')