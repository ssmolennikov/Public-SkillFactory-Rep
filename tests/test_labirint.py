import time
import pytest

from selenium.webdriver.common.alert import Alert
from pages.main_page import MainPage
from pages.search_result_page import SearchResultPage
from pages.compare_page import ComparetPage
from pages.support_page import SupportPage
from pages.help_page import HelpPage
from settings import *


@pytest.mark.positive
def test_checking_the_transition_menu_button_books(driver):  # подтверждено
    """ 01 Проверка перехода из меню главной страницы в Книги. """

    page = MainPage(driver)

    page.menu_button_books.click()  # переход на страницу Книги

    # Проверяем, что переход совершен на соответствующую страницу
    assert page.get_current_url() == url_books  # страница Книги


@pytest.mark.positive
def test_checking_the_transition_menu_button_Main_2022(driver):  # подтверждено
    """ 02 Проверка перехода из меню главной страницы Главное 2022. """

    page = MainPage(driver)
    page.menu_button_Main_2022.click()  # переход на страницу Главное 2022

    # Проверяем, что переход совершен на соответствующую страницу
    assert page.get_current_url() == url_best  # страница Главное 2022


@pytest.mark.positive
def test_checking_the_transition_menu_button_school(driver):  # подтверждено
    """ 03 Проверка перехода из меню главной страницы Школа. """

    page = MainPage(driver)
    page.menu_button_school.click()  # переход на страницу Школа

    # Проверяем, что переход совершен на соответствующую страницу
    assert page.get_current_url() == url_school  # страница Школа


def test_checking_the_transition_menu_games(driver):  # подтверждено
    """ 04 Проверка перехода из меню главной страницы Игрушки. """

    page = MainPage(driver)
    page.menu_button_games.click()  # переход на страницу Игрушки

    # Проверяем, что переход совершен на соответствующую страницу
    assert page.get_current_url() == url_games  # страница Игрушки


def test_checking_the_transition_menu_stationery(driver):  # подтверждено
    """ 05 Проверка перехода из меню главной страницы Канцтовары. """

    page = MainPage(driver)
    page.menu_button_stationery.click()  # переход на страницу Канцтовары

    # Проверяем, что переход совершен на соответствующую страницу
    assert page.get_current_url() == url_office  # страница Канцтовары


def test_checking_the_transition_menu_CD_DVD(driver):  # подтверждено
    """ 06 Проверка перехода из меню главной страницы CD/DVD. """

    page = MainPage(driver)
    page.menu_button_more.click()  # выпадающий список 'Ещё'
    # page.wait_page_loaded()
    page.menu_button_CD_DVD.click()  # переход на страницу CD/DVD

    # Проверяем, что переход совершен на соответствующую страницу
    assert page.get_current_url() == url_multimedia  # страница CD/DVD


def test_checking_the_transition_menu_souvenir(driver):  # подтверждено
    """ 07 Проверка перехода из меню главной страницы Сувениры. """

    page = MainPage(driver)
    page.menu_button_more.click()  # выпадающий список 'Ещё'
    page.menu_button_souvenir.click()  # переход на страницу Сувениры

    # Проверяем, что переход совершен на соответствующую страницу
    assert page.get_current_url() == url_souvenir  # страница Сувениры


def test_checking_the_transition_menu_journals(driver):  # подтверждено
    """ 08 Проверка перехода из меню главной страницы Журналы. """

    page = MainPage(driver)
    page.menu_button_more.click()  # выпадающий список 'Ещё'
    page.menu_button_journals.click()  # переход на страницу Журналы

    # Проверяем, что переход совершен на соответствующую страницу
    assert page.get_current_url() == url_journals  # страница Журналы


def test_checking_the_transition_menu_household_goods(driver):  # подтверждено
    """ 09 Проверка перехода из меню главной страницы Товары для дома. """

    page = MainPage(driver)
    page.menu_button_more.click()  # выпадающий список 'Ещё'
    page.household_goods.click()  # переход на страницу Товары для дома

    # Проверяем, что переход совершен на соответствующую страницу
    assert page.get_current_url() == url_household  # страница Товары для дома


def test_checking_the_transition_menu_club(driver):  # подтверждено
    """ 10 Проверка перехода из меню главной страницы Клуб. """

    page = MainPage(driver)
    # page.menu_button_more.click()  # выпадающий список 'Ещё'
    page.button_club.click()  # переход на страницу Клуб

    # Проверяем, что переход совершен на соответствующую страницу
    assert page.get_current_url() == url_club  # страница Клуб


def test_checking_the_transition_menu_region_location(driver):  #  подтверждено
    """ 11 Проверка изменения региональной локации в меню главной страницы. """

    page = MainPage(driver)
    page.region_location.click()  # открываем
    page.input_region_location.send_keys('Магадан')  # устанавливаем геолокацию
    page.input_region_location.send_keys('\ue007')  # нажимаем Enter (https://www.w3.org/TR/webdriver/#keyboard-actions)
    page.pick_up_points.scroll_to_element()
    page.pick_up_points.click()

    for title in page.input_region_location.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert city in title.lower(), msg  # сравниваем введенную локацию с текущей

    assert page.get_current_url() == url_maps  # проверка текущей страницы


def test_the_transition_from_the_main_page_menu_Delivery_and_payment(driver):  # подтверждено
    """ 12 Проверка перехода из меню главной страницы Доставка и оплата. """

    page = MainPage(driver)
    page.delivery_and_payment.click()  #

    # Проверяем, что переход совершен на соответствующую страницу
    assert page.get_current_url() == url_help  # проверка текущей страницы


def test_transition_from_the_main_page_menu_pick_up_points(driver):  # подтверждено
    """ 13 Проверка перехода из меню главной страницы Пункты самовывоза. """

    page = MainPage(driver)
    page.pick_up_points.click()  #

    # Проверяем, что переход совершен на соответствующую страницу
    assert page.get_current_url() == url_maps  # проверка текущей страницы


@pytest.mark.positive
def test_transition_from_the_author_s_page_to_the_main_page(driver):
    """ 14 Проверка перехода со страницы об авторе на главную."""

    page = MainPage(driver)
    page.search_field.send_keys(author)  # поиск по автору

    page.search_button.click()
    page.wait_page_loaded()

    search_result_page = SearchResultPage(driver, page.get_current_url())
    search_result_page.authors_link.wait_to_be_clickable()

    search_result_page.authors_link.click()  # вкладка "Авторы"

    search_result_page.search_result.click()  # первый автор

    page.logo.wait_to_be_clickable()  # Логотип Лабиринт
    page.logo.click()

    assert page.get_current_url() == main_url


@pytest.mark.positive
def test_transition_from_the_search_page_to_the_main_page(driver):
    """ 15 Проверка перехода со страницы поиска на главную."""

    page = MainPage(driver)
    page.get_first_book_by_name(author_book)

    page.logo.wait_to_be_clickable()
    page.logo.click()

    assert page.get_current_url() == main_url


@pytest.mark.positive
def test_add_to_compare(driver):
    """ 16 Проверка добавления в сравнение."""

    page = MainPage(driver)
    page.accept_cookie.click()
    page.open_actions_block.click()
    page.add_to_compare.wait_to_be_clickable()
    page.add_to_compare.click()
    page.wait_page_loaded()

    # проверяем, название пункта меню меняется на текст 'Перейти к сравнению'
    assert 'Перейти к сравнению' in page.add_to_compare.get_text()


@pytest.mark.positive
def test_delete_from_compare(driver):
    """ 17 Проверка удаления из сравнения."""

    page = MainPage(driver)
    page.accept_cookie.click()
    page.open_actions_block.click()
    page.add_to_compare.wait_to_be_clickable()
    page.add_to_compare.click()
    page.wait_page_loaded()
    page.add_to_compare.click()
    page.wait_page_loaded()
    compare_page = ComparetPage(driver, page.get_current_url())
    compare_page.wait_page_loaded()
    compare_page.delete_compare_list_button.click()
    alert = Alert(driver)
    time.sleep(2)
    alert.accept()

    # проверка после очистки появления текста 'Товаров нет. Добавьте хотя бы один товар, например, из раздела'
    assert 'Товаров нет. Добавьте хотя бы один товар, например, из раздела' in compare_page.empty_compare_text.get_text()


@pytest.mark.xfail
@pytest.mark.positive
def test_transition_from_the_product_comparison_page_to_the_main_page(driver):
    """ 18 Проверка перехода со страницы "Сравнение товаров" на главную."""

    page = MainPage(driver)
    page.accept_cookie.click()
    page.open_actions_block.click()
    page.add_to_compare.wait_to_be_clickable()
    page.add_to_compare.click()
    page.wait_page_loaded()
    page.add_to_compare.click()
    page.wait_page_loaded()
    page.logo.click()

    # проверяем, что вернулись на главную страницу
    assert page.get_current_url() == main_url


@pytest.mark.positive
def test_receipt_of_the_coupon_by_valid_email(driver):
    """ 19 Проверка получения купона по валидному email."""

    page = MainPage(driver)
    page.input_email.send_keys(valid_email)
    page.get_coupon_button.wait_to_be_clickable()
    page.get_coupon_button.click()

    # проверяем, что выводится сообщение 'Адрес электронной почты уже используется'
    assert 'Адрес электронной почты уже используется' in page.get_email_is_in_use_text()


@pytest.mark.negative
def test_receipt_of_the_coupon_by_invalid_email(driver):
    """ 20 Проверка получения купона по невалидному email."""

    page = MainPage(driver)
    page.input_email.send_keys('q@q.q')
    page.get_coupon_button.wait_to_be_clickable()
    page.get_coupon_button.click()

    # проверяем, что выводится сообщение 'Укажите почту'
    assert 'Укажите почту' in page.get_email_is_in_use_text()


@pytest.mark.xfail
@pytest.mark.positive
def test_receipt_of_the_coupon_by_unregistered_valid_email(driver):
    """ 21 Проверка получения купона по незарегистрированному валидному email."""

    page = MainPage(driver)

    page.input_email.send_keys(f'test{time.time()}@test.test')   # cupon@bk.com

    page.get_coupon_button.wait_to_be_clickable()

    page.get_coupon_button.click()

    page.received_coupon_popup.wait_to_be_clickable()

    # проверяем, что выводится сообщение о получении купона
    assert 'Купон на 50 р.' in page.received_coupon_popup.get_text()


@pytest.mark.positive
def test_support_request(driver):
    """ 22 Проверка обращения в поддержку."""

    message_for_support = 'test message'
    page = MainPage(driver)
    page.support_link.click()
    page.wait_page_loaded()
    support_page = SupportPage(driver, page.get_current_url())
    support_page.ask_support_button.wait_to_be_clickable()
    support_page.ask_support_button.click()
    support_page.find_login.wait_to_be_clickable()
    support_page.find_login.send_keys(discount_code)
    support_page.input_button.click()

    support_page.textarea_for_question.send_keys(message_for_support)
    support_page.send_question_button.click()
    support_page.wait_page_loaded()

    assert message_for_support in support_page.posted_question.get_text()


@pytest.mark.negative
def test_send_empty_message_to_support(driver):
    """ 23 Проверка отправления пустого сообщения в поддержку."""

    message_for_support = ''
    support_page = SupportPage(driver)
    support_page.ask_support_button.wait_to_be_clickable()
    support_page.ask_support_button.click()
    support_page.find_login.wait_to_be_clickable()
    support_page.find_login.send_keys(discount_code)
    support_page.input_button.click()
    support_page.textarea_for_question.send_keys(message_for_support)

    support_page.send_question_button.click()
    support_page.send_question_button.click()

    support_page.wait_page_loaded()

    # проверка, что коммуникаций нет
    assert 'Переписки отсутствуют :(' == support_page.no_correspondence_text.get_text()


@pytest.mark.positive
def test_communications_with_word_search_support(driver):
    """ 24 Проверка коммуникаций с поддержкой по поиску слова."""

    message_for_support = 'test message'
    search_request = 'test'
    support_page = SupportPage(driver)
    support_page.ask_support_button.wait_to_be_clickable()
    support_page.ask_support_button.click()
    support_page.find_login.wait_to_be_clickable()
    support_page.find_login.send_keys(discount_code)
    support_page.input_button.click()

    support_page.textarea_for_question.send_keys(message_for_support)
    support_page.send_question_button.click()
    support_page.wait_page_loaded()
    support_page.my_question_link.click()

    support_page.search_here_input.send_keys(search_request)
    support_page.submit_request_button.click()
    support_page.wait_page_loaded()

    # проверяем что в найденных сообщениях содержится искомое слово
    assert search_request in support_page.found_message.get_text()


@pytest.mark.xfail
@pytest.mark.negative
def test_search_for_an_invalid_word_in_support_messages(driver):
    """ 25 Проверка поиска невалидного слова в сообщениях в поддержку."""

    support_page = SupportPage(driver)

    support_page.my_question_link.click()
    support_page.find_login.wait_to_be_clickable()

    support_page.find_login.send_keys(discount_code)

    support_page.input_button.click()
    time.sleep(2)  # в учебных целях
    support_page.wait_page_loaded()
    time.sleep(2)  # в учебных целях
    support_page.search_here_input.send_keys(abracadabra)  # строка поиска сообщений
    time.sleep(2)  # в учебных целях
    support_page.submit_request_button.click()
    support_page.wait_page_loaded()

    # проверка соотвествия сообщения
    assert 'Переписки отсутствуют :(' == support_page.no_correspondence_text.get_text()


@pytest.mark.positive
def test_word_search_in_public_messages_to_support(driver):
    """ 26 Проверка поиска по слову в публичных сообщениях в поддержке."""

    support_page = SupportPage(driver)
    support_page.ask_support_button.wait_to_be_clickable()
    support_page.search_here_input.send_keys(dostav)
    support_page.submit_request_button.click()
    support_page.wait_page_loaded()

    # проверка искомого слова в найденных сообщениях
    assert dostav in support_page.found_message.get_text()


@pytest.mark.negative
def test_search_for_an_invalid_word_in_public_messages_with_support(driver):
    """ 27 Проверка поиска по невалидному слову в публичных сообщениях с поддержкой."""

    support_page = SupportPage(driver)
    support_page.ask_support_button.wait_to_be_clickable()
    support_page.search_here_input.send_keys(abracadabra)
    support_page.submit_request_button.click()
    support_page.wait_page_loaded()

    # проверяем что по найденному запросу сообщения не найдены
    assert 'Переписки отсутствуют' in support_page.not_found_messages_text.get_text()


@pytest.mark.negative
def test_transition_from_the_support_page_to_the_main_page(driver):
    """ 28 Проверка перехода со страницы поддержки на главную."""

    support_page = SupportPage(driver)
    support_page.logo.wait_to_be_clickable()
    support_page.logo.click()

    # проверяем что по нажатию на логотип происходит возврат на главную страницу
    assert support_page.get_current_url() == main_url


@pytest.mark.positive
def test_word_search_on_the_help_page(driver):
    """ 29 Проверка поиска по слову на странице Помощи."""

    help_page = HelpPage(driver)
    help_page.search_input.wait_to_be_clickable()
    help_page.search_input.send_keys(dostavka)

    help_page.find_button.click()
    help_page.wait_page_loaded()

    search_request_in_head_found_post = dostavka in help_page.found_post_head.get_text()
    search_request_in_body_found_post = dostavka in help_page.found_post_body_preview.get_text()

    # проверка искомого слова в сообщениях
    assert search_request_in_head_found_post or search_request_in_body_found_post


@pytest.mark.negative
def test_search_for_an_invalid_word_on_the_Help_page(driver):
    """ 30 Проверка поиска по невалидному слову на странице Помощи."""

    help_page = HelpPage(driver)

    help_page.search_input.wait_to_be_clickable()

    help_page.search_input.send_keys(abracadabra)

    help_page.find_button.click()

    help_page.wait_page_loaded()

    # проверяем что по запросу ничего не нашлось
    assert 'Поиск в разделе Помощь не дал результатов' in help_page.not_found_post_message.get_text()


@pytest.mark.positive
def test_transition_from_the_help_page_to_the_main_page(driver):
    """ 31 Проверка перехода со страницы Помощи на главную."""

    help_page = HelpPage(driver)

    help_page.logo.wait_to_be_clickable()

    help_page.logo.click()

    # проверяем что по нажатию на логотип происходит возврат на главную страницу
    assert help_page.get_current_url() == main_url


@pytest.mark.positive
def test_checking_the_transition_menu_button_books_faraway(driver):  # подтверждено
    """ 32 Проверка перехода из меню главной страницы в Книги. """

    page = MainPage(driver)

    page.menu_button_books.find()  # поиск Книги

    page.menu_button_books.scroll_to_element()  # скролл к Книги

    # Проверяем, что переход совершен на соответствующую страницу
    assert page.get_current_url() == url_books  # страница Книги