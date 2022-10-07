import pytest
import time

from selenium.webdriver.common.alert import Alert
from pages.main_page import MainPage
from pages.search_result_page import SearchResultPage
from pages.favorites_page import FavoritesPage
from settings import *


@pytest.mark.positive
def test_for_the_absence_of_deferred_items(driver):
    """ 01 p Проверка отсутствия отложенных товаров."""

    page = MainPage(driver)

    page.postponed_mp.click()
    page.wait_page_loaded()

    favorites_page = FavoritesPage(driver)
    favorites_page.no_favorite_goods.wait_to_be_clickable()

    assert 'Отложите интересные вам товары' in favorites_page.no_favorite_goods.get_text()


@pytest.mark.positive
def test_transition_from_the_deferred_droducts_page_to_the_main_page(driver):
    """ 02 p Проверка перехода со страницы Отложенные товары на главную."""

    page = MainPage(driver)

    page.postponed_mp.click()  # кнопка Отложено

    page.logo.wait_to_be_clickable()
    page.logo.click()

    assert page.get_current_url() == main_url


@pytest.mark.positive
def test_adding_to_deferred_from_the_search_page(driver):
    """ 03 p Проверка добавление в отложенное со страницы поиска."""

    page = MainPage(driver)

    _, _, add_to_favorite, _ = page.get_first_book_by_name(author_book)  # идем Отложено
    add_to_favorite.click()  # добавляем в избранное (отложено)

    page.postponed_counter_mp.wait_to_be_clickable()
    postponed_counter = int(page.postponed_counter_mp.get_text())

    assert postponed_counter > 0  # проверяем отсутствие отложенных товаров

    page.add_to_favorite_popup.wait_to_be_clickable()

    assert 'Вы добавили в отложенные книгу' in page.add_to_favorite_popup.get_text()


@pytest.mark.positive
def test_for_deletion_from_the_deferred_from_the_search_page(driver):
    """ 04 p Проверка удаления из отложенного со страницы поиска."""

    page = MainPage(driver)

    _, _, add_to_favorite, _ = page.get_first_book_by_name(author_book)  # идем к Отложено
    page.wait_page_loaded()

    search_result_page = SearchResultPage(driver, page.get_current_url())
    add_to_favorite.wait_to_be_clickable()

    add_to_favorite.click()
    add_to_favorite.click()  # вызов контекстного меню
    search_result_page.delete_from_favorite.wait_to_be_clickable()
    search_result_page.delete_from_favorite.click()  # нажимаем на вторую кнопку в меню

    page.postponed_counter_mp.wait_to_be_clickable()
    postponed_counter = int(page.postponed_counter_mp.get_text())

    assert postponed_counter == 0


@pytest.mark.positive
@pytest.mark.xfail(reason="The quantity counter does not always show!")
def test_deletion_from_the_deferred_with_the_clear_button(driver):
    """ 05 p Проверка удаления из отложенного кнопкой Очистить."""

    page = MainPage(driver)

    _, _, add_to_favorite, _ = page.get_first_book_by_name(author_book)  # выбор книги по автору

    add_to_favorite.click()  # добавляем товар в отложено

    page.accept_cookie.click()  # принять

    page.postponed_counter_mp.click()  # количество отложенных товаров и переход в Отложено

    page.wait_page_loaded()

    favorite_page = FavoritesPage(driver, page.get_current_url())
    time.sleep(3)
    favorite_page.select_all_postponded.wait_to_be_clickable()
    favorite_page.select_all_postponded.click()  # выбрать все
    time.sleep(3)
    favorite_page.clear_favorite.wait_to_be_clickable()
    time.sleep(3)
    favorite_page.clear_favorite.click()  # удаляем товара из Отложено
    time.sleep(3)
    alert = Alert(driver)  # оповещающий объект
    time.sleep(3)
    alert.accept()  # нажимаем "Ок" на окне

    favorite_page.refresh()

    assert favorite_page.postponed_counter_fp.get_text == '0'