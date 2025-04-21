"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from library.views.apis.books import BooksAPIView
from library.views import book, author, publisher


urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', book.books_list, name='books_list'),
    path('books/add/', book.add_book, name='add_book'),
    path('authors/add/', author.add_author, name='add_author'),
    path('publishers/add/', publisher.add_publisher, name='add_publisher'),

    path('api/books/', BooksAPIView.as_view(), name="books_api"),
]
