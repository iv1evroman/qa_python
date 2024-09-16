from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_adding_new_book(self):
        collector_1 = BooksCollector()
        collector_1.add_new_book('1984')
        assert collector_1.books_genre.get('1984') == ''

    def test_set_book_genre_setting_fantasy_genre(self):
        collector_2 = BooksCollector()
        collector_2.add_new_book('1984')
        collector_2.set_book_genre('1984', 'Фантастика')
        assert collector_2.books_genre.get('1984') == 'Фантастика'

    def test_get_book_genre_getting_book_genre_by_its_name(self):
        collector_3 = BooksCollector()
        collector_3.add_new_book('1984')
        collector_3.set_book_genre('1984', 'Фантастика')
        assert collector_3.get_book_genre('1984') == 'Фантастика'

    def test_get_books_with_specific_genre_getting_fantasy_genre_book(self):
        collector_4 = BooksCollector()
        collector_4.add_new_book('1984')
        collector_4.set_book_genre('1984', 'Фантастика')
        assert collector_4.get_books_with_specific_genre('Фантастика') == ['1984']

    def test_get_books_genre_getting_books_genre(self):
        collector_5 = BooksCollector()
        collector_5.add_new_book('1984')
        collector_5.set_book_genre('1984', 'Фантастика')
        assert collector_5.get_books_genre() == {'1984' : 'Фантастика'}

    def test_get_books_for_children_getting_book_without_age_rating(self):
        collector_6 = BooksCollector()
        collector_6.add_new_book('1984')
        collector_6.set_book_genre('1984', 'Фантастика')
        collector_6.add_new_book('Убийства и кексики')
        collector_6.set_book_genre('Убийства и кексики', 'Детективы')
        assert collector_6.get_books_for_children() == ['1984']

    def test_add_book_in_favorites_add_book_from_books_genre(self):
        collector_7 = BooksCollector()
        collector_7.add_new_book('1984')
        collector_7.add_book_in_favorites('1984')
        assert collector_7.favorites == ['1984']

    def test_delete_book_from_favorites_delete_book_which_is_in_favourites(self):
        collector_8 = BooksCollector()
        collector_8.add_new_book('1984')
        collector_8.add_book_in_favorites('1984')
        collector_8.delete_book_from_favorites('1984')
        assert collector_8.favorites == []

    def test_get_list_of_favorites_books_get_list_of_books_from_favorites(self):
        collector_9 = BooksCollector()
        collector_9.add_new_book('1984')
        collector_9.add_book_in_favorites('1984')
        collector_9.add_new_book('Убийства и кексики')
        collector_9.add_book_in_favorites('Убийства и кексики')
        assert collector_9.get_list_of_favorites_books() == ['1984', 'Убийства и кексики']



