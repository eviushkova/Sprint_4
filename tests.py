import pytest


class TestBooksCollector:

    def test_add_new_book_one_book_added(self, collector):
        collector.add_new_book('Приключения Шерлока Холмса')

        assert 'Приключения Шерлока Холмса' in collector.books_genre

    def test_set_book_genre_set_existing_genre(self, collector):
        collector.add_new_book('Сияние')
        collector.set_book_genre('Сияние', 'Ужасы')

        assert collector.books_genre['Сияние'] == 'Ужасы'

    def test_get_book_genre_get_existing_genre(self, collector):
        collector.add_new_book('Дюна')
        collector.set_book_genre('Дюна', 'Фантастика')

        assert collector.get_book_genre('Дюна') == 'Фантастика'

    @pytest.mark.parametrize('book_to_genre, requested_genre, expected_result', [
        [{'Дюна': 'Фантастика', 'Властелин Колец': 'Фантастика'}, 'Фантастика', ['Дюна', 'Властелин Колец']]
    ])
    def test_get_books_with_specific_genre_existing_books(self, collector, book_to_genre, requested_genre,
                                                          expected_result):
        for key, value in book_to_genre.items():
            collector.add_new_book(key)
            collector.set_book_genre(key, value)
        books_result = collector.get_books_with_specific_genre(requested_genre)

        assert books_result == expected_result

    def test_get_books_genre_get_existing_genre(self, collector):
        collector.add_new_book('Собака Баскервилей')
        collector.set_book_genre('Собака Баскервилей', 'Детективы')
        books_genre_result = collector.books_genre

        assert books_genre_result == {'Собака Баскервилей': 'Детективы'}

    @pytest.mark.parametrize('books_and_genres, expected_result', [
        [{'Малыш и Карлсон': 'Мультфильмы', 'Винни-Пух': 'Мультфильмы'}, ['Малыш и Карлсон', 'Винни-Пух']]
    ])
    def test_get_books_for_children_return_expected_books(self, collector, books_and_genres, expected_result):
        for key, value in books_and_genres.items():
            collector.add_new_book(key)
            collector.set_book_genre(key, value)
        book_for_children_result = collector.get_books_for_children()

        assert book_for_children_result == expected_result

    def test_add_book_in_favorites_add_one_book_to_favorites(self, collector):
        collector.add_new_book('Собака Баскервилей')
        collector.set_book_genre('Собака Баскервилей', 'Детективы')
        collector.add_book_in_favorites('Собака Баскервилей')

        assert 'Собака Баскервилей' in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_one_book_delete_from_favorites(self, collector):
        collector.books_genre = {'Малыш и Карлсон': 'Мультфильмы', 'Винни-Пух': 'Мультфильмы'}
        collector.add_book_in_favorites('Малыш и Карлсон')
        collector.add_book_in_favorites('Винни-Пух')
        collector.delete_book_from_favorites('Малыш и Карлсон')

        assert 'Винни-Пух' in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books_two_books_in_list_of_favorites(self, collector):
        collector.books_genre = {'Малыш и Карлсон': 'Мультфильмы', 'Винни-Пух': 'Мультфильмы'}
        collector.add_book_in_favorites('Малыш и Карлсон')
        collector.add_book_in_favorites('Винни-Пух')
        favorite_books = collector.get_list_of_favorites_books()

        assert favorite_books == ['Малыш и Карлсон', 'Винни-Пух']

    def test_get_list_of_favorites_books_zero_books_in_list_of_favorites(self, collector):
        collector.books_genre = {'Малыш и Карлсон': 'Мультфильмы', 'Винни-Пух': 'Мультфильмы'}
        favorite_books = collector.get_list_of_favorites_books()

        assert favorite_books == []

