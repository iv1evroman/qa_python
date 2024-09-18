from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test


class TestBooksCollector:
    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
    import pytest

    @pytest.mark.parametrize('book_name', ['1984'])
    def test_add_new_book_adding_new_book(self, collector, book_name):
        collector.add_new_book(book_name)
        assert collector.books_genre.get(book_name) == ''

    @pytest.mark.parametrize('book_name,genre', [['1984', 'Фантастика']])
    def test_set_book_genre_setting_fantasy_genre(self, book_name, genre):
        collector_2 = BooksCollector()
        collector_2.add_new_book(book_name)
        collector_2.set_book_genre(book_name, genre)
        assert collector_2.books_genre.get(book_name) == genre

    @pytest.mark.parametrize('book_name,genre', [['1984', 'Фантастика']])
    def test_get_book_genre_getting_book_genre_by_its_name(self, book_name, genre):
        collector_3 = BooksCollector()
        collector_3.add_new_book(book_name)
        collector_3.set_book_genre(book_name, genre)
        assert collector_3.get_book_genre(book_name) == genre

    @pytest.mark.parametrize('book_name,genre', [['1984', 'Фантастика']])
    def test_get_books_with_specific_genre_getting_fantasy_genre_book(self, book_name, genre):
        collector_4 = BooksCollector()
        collector_4.add_new_book(book_name)
        collector_4.set_book_genre(book_name, genre)
        assert collector_4.get_books_with_specific_genre(genre) == [book_name]

    @pytest.mark.parametrize('book_name,genre', [['1984', 'Фантастика']])
    def test_get_books_genre_getting_books_genre(self, book_name, genre):
        collector_5 = BooksCollector()
        collector_5.add_new_book(book_name)
        collector_5.set_book_genre(book_name, genre)
        assert collector_5.get_books_genre() == {book_name: genre}

    @pytest.mark.parametrize('book_name,genre', [['1984', 'Фантастика']])
    def test_get_books_for_children_getting_book_without_age_rating(self, book_name, genre):
        collector_6 = BooksCollector()
        collector_6.add_new_book(book_name)
        collector_6.set_book_genre(book_name, genre)
        assert collector_6.get_books_for_children() == [book_name]

    @pytest.mark.parametrize('book_name', ['1984'])
    def test_add_book_in_favorites_add_book_from_books_genre(self, book_name):
        collector_7 = BooksCollector()
        collector_7.add_new_book(book_name)
        collector_7.add_book_in_favorites(book_name)
        assert collector_7.favorites == [book_name]

    @pytest.mark.parametrize('book_name', ['1984'])
    def test_delete_book_from_favorites_delete_book_which_is_in_favourites(self, book_name):
        collector_8 = BooksCollector()
        collector_8.add_new_book(book_name)
        collector_8.add_book_in_favorites(book_name)
        collector_8.delete_book_from_favorites(book_name)
        assert collector_8.favorites == []

    @pytest.mark.parametrize('book_name', ['1984', 'Убийства и кексики'])
    def test_get_list_of_favorites_books_get_list_of_books_from_favorites(self, book_name):
        collector_9 = BooksCollector()
        collector_9.add_new_book(book_name)
        collector_9.add_book_in_favorites(book_name)
        assert collector_9.get_list_of_favorites_books() == [book_name]
