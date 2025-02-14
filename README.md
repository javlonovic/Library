# My Django Project

This is a Django project for managing and posting new books. The application allows users to log in, sign up, and chat with each other. It also provides information about the 300th school located in Tashkent, Uzbekistan.

## Project Structure

```
my-django-project
├── my_django_project
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── books
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── views.py
│   ├── urls.py
│   └── templates
│       └── books
│           ├── base.html
│           ├── home.html
│           ├── login.html
│           ├── signup.html
│           ├── chat.html
│           ├── about_us.html
│           └── book_list.html
├── manage.py
└── README.md
```

## Features

- User authentication (login and signup)
- Chat functionality for students
- Information page about the 300th school in Tashkent, Uzbekistan
- Responsive design using Bootstrap and custom CSS
- Interactive elements with JavaScript animations

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/my-django-project.git
   ```

2. Navigate to the project directory:
   ```
   cd my-django-project
   ```

3. Create a virtual environment:
   ```
   python -m venv venv
   ```

4. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
5. Run the migrations:
   ```
   python manage.py migrate
   ```

6. Start the development server:
   ```
   python manage.py runserver
   ```

## Usage

- Access the application at `http://127.0.0.1:8000/`
- Use the navigation bar to access different pages (Home, Chat, About Us).
- Users can log in or sign up to access chat functionality.

## License

This project is licensed under the MIT License.
