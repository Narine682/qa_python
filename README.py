import pytest
from main import BooksCollector

@pytest.fixture
def collector():
    return BooksCollector()

def test_add_new_book_adds_book_without_genre(collector):
    collector.add_new_book("Гарри Поттер")
    assert collector.get_books_genre() == {"Гарри Поттер": ""}

@pytest.mark.parametrize("invalid_name", ["", "A" * 41])
def test_cannot_add_book_with_invalid_name(collector, invalid_name):
    collector.add_new_book(invalid_name)
    assert invalid_name not in collector.get_books_genre()

def test_add_new_book_cannot_add_duplicate(collector):
    collector.add_new_book("Книга")
    collector.set_book_genre("Книга", "Поэзия")
    assert collector.get_book_genre("Книга") == ''

def test_get_book_returns_none_for_unknown_book(collector):
    assert  collector.get_book_genre("Несуществующая книга") is None

def test_get_books_with_specific_genre_returns_only_that_genre(collector):
    collector.add_new_book("A"); collector.set_book_genre("A", "Фантастика")
    collector.add_new_book("B"); collector.set_book_genre("B", "Комедии")
    collector.add_new_book("C"); collector.set_book_genre("C", "Фантастика")
    assert set(collector.get_books_with_specific_genre("Фантастика")) == {"A", "C"}

def test_get_books_genre_return_full_dict(collector):
    collector.add_new_book("A")
    collector.add_new_book("B");collector.set_book_genre("B", "Комедии")
    assert collector.get_books_genre() == {"A": "", "B": "Комедии"}

def test_delete_book_from_favorites_removes_book(collector):
    collector.add_new_book("Книга")
    collector.add_book_in_favorites("Книга")
    collector.delete_book_from_favorites("Книга")
    assert collector.get_list_of_favorites_books() == []

def test_get_book_for_children_filters_out_age_restricted(collector):
    collector.add_new_book("Смешарики"); collector.set_book_genre("Смешарики", "Мультфильмы")
    collector.add_new_book("Шерлок"); collector.set_book_genre("Шерлок", "Детективы")
    assert  collector.get_books_for_children() == ["Смешарики"]

def test_get_books_with_specific_genre_returns_empty_if_none(collector):
    collector.add_new_book("Книга")
    collector.set_book_genre("Книга", "Фантастика")
    assert  collector.get_books_with_specific_genre("Комедии") == []









