from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from .models import User, Book, Message
from .forms import SignUpForm, LoginForm, MessageForm

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'books/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'books/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

@login_required
def home(request):
    class_grade = request.GET.get('class_grade')
    if class_grade:
        books = Book.objects.filter(class_grade=class_grade)
    else:
        books = Book.objects.all()
    return render(request, 'books/home.html', {'books': books})

@login_required
def book_detail(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    trending_books = Book.objects.filter(is_trending=True).exclude(id=book_id)
    return render(request, 'books/book_detail.html', {'book': book, 'trending_books': trending_books})

@login_required
def chat_view(request):
    messages = Message.objects.all()
    return render(request, 'books/chat.html', {'messages': messages})

@login_required
def send_message(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.user = request.user
            message.save()
            return redirect('chat')
    else:
        form = MessageForm()
    return render(request, 'books/chat.html', {'form': form})

@login_required
def edit_message(request, message_id):
    message = get_object_or_404(Message, id=message_id)
    if request.method == 'POST':
        form = MessageForm(request.POST, instance=message)
        if form.is_valid():
            form.save()
            return redirect('chat')
    else:
        form = MessageForm(instance=message)
    return render(request, 'books/edit_message.html', {'form': form})

def about_us(request):
    return render(request, 'books/about_us.html')

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def error_404(request, exception):
    return render(request, 'books/404.html', status=404)