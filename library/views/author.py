from django.shortcuts import redirect, render

from library.forms import AuthorForm


def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_book')

    else:
        form = AuthorForm()

    return render(request, 'add_author.html', {'form': form})