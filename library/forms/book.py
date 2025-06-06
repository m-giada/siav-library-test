from django import forms

from library.models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'authors', 'publisher']
        widgets = {
            'authors': forms.SelectMultiple()
        }