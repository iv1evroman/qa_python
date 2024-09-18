
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

    @pytest.mark.parametrize('book_name', ['1984', 'Я', 'Гарри Поттер'])
    def test_add_new_book_adding_new_book(self, collector, book_name):
        collector.add_new_book(book_name)
        assert collector.books_genre.get(book_name) == ''

    def test_set_book_genre_setting_fantasy_genre(self, collector):
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.books_genre.get('1984') == 'Фантастика'

    def test_get_book_genre_getting_book_genre_by_its_name(self, collector):
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.get_book_genre('1984') == 'Фантастика'

    def test_get_books_with_specific_genre_getting_fantasy_genre_book(self, collector):
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.get_books_with_specific_genre('Фантастика') == ['1984']

    def test_get_books_genre_getting_books_genre(self, collector):
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Фантастика')
        assert collector.get_books_genre() == {'1984': 'Фантастика'}

    def test_get_books_for_children_getting_book_with_age_rating(self, collector):
        collector.add_new_book('1984')
        collector.set_book_genre('1984', 'Ужасы')
        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_add_book_from_books_genre(self, collector):
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        assert collector.favorites == ['1984']

    def test_delete_book_from_favorites_delete_book_which_is_in_favourites(self, collector):
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        collector.delete_book_from_favorites('1984')
        assert collector.favorites == []

    def test_get_list_of_favorites_books_get_list_of_books_from_favorites(self, collector):
        collector.add_new_book('1984')
        collector.add_book_in_favorites('1984')
        assert collector.get_list_of_favorites_books() == ['1984']
