from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('logout/', views.logout_view, name='logout'),
    path('chat/', views.chat_view, name='chat'),
    path('about/', views.about_us, name='about_us'),
    path('books/', views.book_list, name='book_list'),
    path('books/<int:book_id>/', views.book_detail, name='book_detail'),
    path('send_message/', views.send_message, name='send_message'),
    path('edit_message/<int:message_id>/', views.edit_message, name='edit_message'),
]

handler404 = 'books.views.error_404'