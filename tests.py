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
    # тест для проверки добавления рейтинга
    def test_set_book_rating_add_rating_to_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 2)
        assert collector.books_rating['Гордость и предубеждение и зомби'] == 2

    #получаем рейтинг книги по ее имени
    def test_get_book_rating_getting_book_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 2)
        collector.get_book_rating('Гордость и предубеждение и зомби')
        assert collector.books_rating.get('Гордость и предубеждение и зомби') == 2

    # выводим список книг с определенным рейтингом
    def test_get_books_with_specific_rating_get_list(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 2)
        collector.add_new_book('Война и мир')
        collector.set_book_rating('Война и мир', 10)
        collector.add_new_book('тестирование дот ком')
        collector.set_book_rating('тестирование дот ком', 2)
        collector.get_books_with_specific_rating(2)
        assert len(collector.get_books_with_specific_rating(2)) == 2

    # получаем словарь books_rating
    def test_get_books_rating_get_dictionary(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.set_book_rating('Гордость и предубеждение и зомби', 2)
        assert type(collector.books_rating) is dict and 'Гордость и предубеждение и зомби' in collector.books_rating

    # добавляем книгу в Избранное
    def test_add_book_in_favorites_add_book_in_list(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        assert 'Гордость и предубеждение и зомби' in collector.favorites

    # удаляем книгу из Избранного
    def test_delete_book_from_favorites_delete_book(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_new_book('Тестирование дот ком')
        collector.add_book_in_favorites('Тестирование дот ком')
        collector.delete_book_from_favorites('Гордость и предубеждение и зомби')
        assert len(collector.favorites) == 1

    # получаем список Избранных книг
    def test_list_of_favorites_books_add_book_in_faivorits(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_book_in_favorites('Гордость и предубеждение и зомби')
        collector.add_new_book('Тестирование дот ком')
        collector.add_book_in_favorites('Тестирование дот ком')
        assert type(collector.favorites) is list and 'Гордость и предубеждение и зомби' in collector.favorites
