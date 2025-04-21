import json

from django.core.management import BaseCommand

from library.requests.authors import CreateAuthorRequest
from library.requests.books import CreateBookRequest
from library.requests.publishers import CreatePublisherRequest
from library.usecases.save_author import SaveAuthorUseCase
from library.usecases.save_book import SaveBookUseCase
from library.usecases.save_publisher import SavePublisherUseCase


class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('json_path', type=str, help='Path to the JSON file')

    def handle(self, *args, **kwargs):
        json_path = kwargs['json_path']

        with open(json_path, 'r', encoding='utf-8') as file:
            data = json.load(file)

        try:
            self._save_publishers(data['editori'])
            self._save_authors(data['autori'])
            self._save_books(data['libri'])
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'An error occurred while saving file data. {e}'))

        self.stdout.write(self.style.SUCCESS('Import completed successfully.'))


    def _save_publishers(self, publishers):
        for publisher in publishers:
            publisher_request = CreatePublisherRequest(
                business_name=publisher.get('ragione sociale'),
                address=publisher.get('indirizzo', ''),
                phone_number=publisher.get('telefono', ''),
            )
            p = SavePublisherUseCase.execute(request=publisher_request)
            self.stdout.write(self.style.SUCCESS(f'Publisher {p.business_name} successfully saved.'))

    def _save_authors(self, authors):
        for author in authors:
            author_request = CreateAuthorRequest(
                first_name=author.get('nome'),
                last_name=author.get('cognome'),
            )
            a = SaveAuthorUseCase.execute(request=author_request)
            self.stdout.write(self.style.SUCCESS(f'Author {a.first_name} successfully saved.'))

    def _save_books(self, books):
        for book in books:
            book_request = CreateBookRequest(
                title=book.get('titolo'),
                publisher_id=book.get('editore'),
                author_ids=[book.get('autore')],
                publication_year=book.get('anno edizione'),
            )
            b = SaveBookUseCase.execute(request=book_request)
            self.stdout.write(self.style.SUCCESS(f'Book {b.title} successfully saved.'))