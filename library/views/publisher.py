from django.shortcuts import redirect, render

from library.forms import PublisherForm


def add_publisher(request):
    if request.method == 'POST':
        form = PublisherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_book')

    else:
        form = PublisherForm()

    return render(request, 'add_publisher.html', {'form': form})