from django.shortcuts import redirect, render

from library.forms import BookForm
from library.models import Book


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books_list')
    else:
        form = BookForm()

    return render(request, 'add_book.html', {'form': form})


def books_list(request):
    books = Book.objects.all().order_by('publication_year')
    return render(request, 'books_list.html', {'books': books})