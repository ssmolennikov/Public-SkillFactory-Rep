import pytest
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.main_page import MainPage
from pages.about_book_page import AboutBookPage
from pages.about_author_page import AboutAuthorPage
from pages.search_result_page import SearchResultPage
from pages.web_element import ManyWebElements
from settings import *


@pytest.mark.positive
def test_search_by_author(driver):
    """ 01 s Проверка поиска по автору."""

    page = MainPage(driver)
    page.search_field.send_keys(author)  # поиск по автору

    page.search_button.click()  # кнопка Искать
    page.wait_page_loaded()

    search_result_page = SearchResultPage(driver, page.get_current_url())  # передаем управление классу SearchResultPage
    search_result_page.wait_page_loaded()

    search_result_page.authors_link.click()  # вкладка "Авторы"

    search_result_page.found_author.click()  # первый автор в списке результатов
    about_author_page = AboutAuthorPage(driver, page.get_current_url())  # передаем управление классу AboutAuthorPage
    about_author_page.author_name.wait_to_be_clickable()

    # Проверка соответствия автора
    assert about_author_page.author_name.get_text() == author


@pytest.mark.positive
def test_search_by_book(driver):
    """ 02 s Проверка поиска по названию книги."""

    page = MainPage(driver)
    book_name, _, _, _ = page.get_first_book_by_name(author_book)

    assert author_book in book_name.get_text()

@pytest.mark.positive
def test_search_by_isbn(driver):
    """ 03 s Проверка поиска книги по ISBN."""

    page = MainPage(driver)
    book_name, _, _, _ = page.get_first_book_by_name(book_isbn)
    assert "Мцыри" in book_name.get_text()

    book_name.click()
    # page.wait_page_loaded()
    about_book = AboutBookPage(driver, page.get_current_url())
    time.sleep(3)
    about_book.isbn.wait_to_be_clickable()

    assert book_isbn in about_book.isbn.get_text()


@pytest.mark.negative
def test_invalid_search(driver):
    """ 04 s Проверка поиска по невалидному запросу."""

    page = MainPage(driver)

    page.search_field.send_keys(repeating_letter)
    page.search_button.click()
    page.wait_page_loaded()

    search_result_page = SearchResultPage(driver, page.get_current_url())
    search_result_page.not_found_issue.wait_to_be_clickable()

    assert search_result_page.not_found_issue.get_text() == 'Мы ничего не нашли по вашему запросу! Что делать?'


# @pytest.mark.xfail
@pytest.mark.positive
def test_checking_the_search(driver):
    """ 05 s Проверка поиска (комиксы)."""

    page = MainPage(driver)

    page.search_field = search_random_valid  # поле поиска
    page.search_button.click()  # кнопка Искать
    page.wait_page_loaded()
    time.sleep(3)  # в учебных целях

    count_elem = page.products_titles

    # проверка количества товаров на странице
    assert count_elem.count() == 60, 'Не выведены первые 60 результатов'


@pytest.mark.positive
def test_success_of_the_search_for_a_valid_query(driver):
    """ 06 s Проверка успешности поиска по валидному запросу."""

    page = MainPage(driver)

    page.search_field.send_keys(search_random_valid)  # отправляем запрос в поисковй строке 'Детям'
    page.search_button.click()
    page.wait_page_loaded()  # ожидаем

    # Проверка успешности запроса - "Все, что мы нашли в Лабиринте по запросу"
    assert page.successful_search


@pytest.mark.positive
def test_filter_search_in_stock(driver):
    """ 07 s Проверка поиска по фильтру в наличии."""

    page = MainPage(driver)
    page.search_field.send_keys(book_it)
    page.search_button.click()

    page.all_filers.click()  # все фильтры
    page.reset_all_filers.click()
    page.available.click()
    page.show_all_found.click()
    element = WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.XPATH, '//*[@class="btn buy-link btn-primary"]'))
    )

    assert element


@pytest.mark.positive
def test_search_by_filter_is_not_on_sale(driver):
    """ 08 s Проверка поиска по фильтру нет в продаже."""

    page = MainPage(driver)
    page.search_field.send_keys(book_it)
    page.search_button.click()
    page.all_filers.click()
    page.reset_all_filers.click()
    page.not_available.click()
    page.show_all_found.click()

    element = WebDriverWait(driver, 10).until(
        EC.invisibility_of_element_located((By.XPATH, '//span[text()="Нет в продаже"]'))
    )

    assert element


@pytest.mark.positive
def test_search_by_products_and_genres(driver):
    """ 09 s Проверка поиска по товарам и жанрам."""

    page = MainPage(driver)

    page.search_field.send_keys(search_it)  # ищем Программирование
    page.search_button.click()

    page.wait_page_loaded()  # ожидаем загрузку страницы

    # находимся на соответствующей странице
    assert page.get_current_url() == url_search_1


@pytest.mark.positive
def test_search_by_topic_theme(driver):
    """ 10 s Проверка поиска по теме."""

    page = MainPage(driver)

    page.search_field.send_keys(search_it)
    page.search_button.click()

    page.wait_page_loaded()

    page.search_result_genres.click()

    assert page.get_current_url() == url_search_result_genres




