import json
from unittest import TestCase
from unittest.mock import patch

from django.test import Client
from rest_framework import status

from library.dtos.authors import AuthorDTO
from library.dtos.books import BookDTO
from library.dtos.pagination import PaginationDTO
from library.dtos.publishers import PublisherDTO
from library.requests.books import ListBooksRequest, CreateBookRequest


class BooksAPIViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.mock_book_dto = BookDTO(
            id=1,
            title='Book 1',
            publication_year=2024,
            publisher=PublisherDTO(
                id=10,
                business_name='<NAME>',
                address='123 Main St.',
            ),
            authors=[
                AuthorDTO(
                    id=5,
                    first_name='<NAME>',
                    last_name='<SURNAME>',
                )
            ]
        )

    @patch('library.usecases.list_books.ListBooksUseCase.execute')
    def test_get_books_list(self, mock_usecase):
        mock_usecase.return_value = PaginationDTO(
            total_count=1,
            page=1,
            page_size=10,
            results=[self.mock_book_dto],
        )

        response = self.client.get('/api/books/', {'page': 1, 'page_size': 10})

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(response.data)
        self.assertEqual(response.data['page'], 1)
        self.assertEqual(response.data['page_size'], 10)
        self.assertEqual(response.data['total_count'], 1)
        self.assertEqual(len(response.data['results']),1)
        self.assertEqual(response.data['results'][0]['id'], self.mock_book_dto.id)
        self.assertEqual(response.data['results'][0]['title'], self.mock_book_dto.title)
        mock_usecase.assert_called_once()
        mock_usecase.assert_called_with(request=ListBooksRequest(page=1, page_size=10))

    @patch('library.usecases.save_book.SaveBookUseCase.execute')
    def test_save_book(self, mock_usecase):
        mock_usecase.return_value = self.mock_book_dto
        request_data = {
                            "title": self.mock_book_dto.title,
                            "author_ids": [self.mock_book_dto.authors[0].id],
                            "publisher_id": self.mock_book_dto.publisher.id,
                            "publication_year": self.mock_book_dto.publication_year,
                        }
        response = self.client.post('/api/books/',
                                    data=json.dumps(request_data),
                                    content_type='application/json'
                                    )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIsNotNone(response.data)
        self.assertEqual(response.data['id'], self.mock_book_dto.id)
        self.assertEqual(response.data['title'], self.mock_book_dto.title)
        self.assertEqual(response.data['publication_year'], self.mock_book_dto.publication_year)
        self.assertEqual(response.data['publisher']['id'], self.mock_book_dto.publisher.id)
        self.assertEqual(response.data['authors'][0]['id'], self.mock_book_dto.authors[0].id)
        mock_usecase.assert_called_once()
        mock_usecase.assert_called_with(
            request=CreateBookRequest(
                title=self.mock_book_dto.title,
                author_ids=[self.mock_book_dto.authors[0].id],
                publisher_id=self.mock_book_dto.publisher.id,
                publication_year=self.mock_book_dto.publication_year,
            )
        )
