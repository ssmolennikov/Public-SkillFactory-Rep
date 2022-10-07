import pytest

from pages.main_page import MainPage
from settings import *


@pytest.mark.positive
def test_authorization_with_valid_values(driver):
    """ 01 auth Проверка авторизации с валидными значениями."""

    page = MainPage(driver)

    page.main_cabinet.click()  # кнопка Мой Лаб

    page.other_ways_to_login.click()  # кнопка 'Другие способы входа'

    page.mail_login_button.click()  # кнопка "Mail.ru"
    page.my_mail_login_input.send_keys(valid_email)  # поле для ввода логина

    page.my_mail_enter_button.click()

    page.my_mail_password_input.send_keys(valid_password)

    page.my_mail_enter_button.click()

    # page.allow_my_mail_next_button.click()  # разрешение при первом входе

    page.user_name.wait_to_be_clickable()

    assert page.user_name.get_text() == login_test


@pytest.mark.positive
def test_authorization_by_the_correct_discount_code(driver):
    """ 02 auth Проверка авторизации по корректному коду скидки."""

    page = MainPage(driver)
    page.main_cabinet.click()

    page.other_ways_to_login.click()

    page.find_login.send_keys(discount_code)  # код скидки
    page.input_button.click()

    page.wait_page_loaded()
    page.user_name.wait_to_be_clickable()  # имя авторизаванного пользователя

    # проверяем, что в шапке сайта появилось имя авторизаванного пользователя
    assert page.user_name.get_text() == login


@pytest.mark.negative
@pytest.mark.parametrize("invalid_symbol", [' ', '!', '#', '$'], ids=['space', '!', '#', '$'])
def test_login_input_of_4_incorrect_characters(driver, invalid_symbol):
    """ 03 auth Проверка ввода 4 некорректных символов."""

    page = MainPage(driver)

    page.main_cabinet.click()

    page.find_login.send_keys(invalid_symbol)

    assert page.login_error_message.get_text() == f"Нельзя использовать символ «{invalid_symbol}»"


@pytest.mark.negative
def test_login_validation_when_entering_incorrect_code(driver):
    """ 04 auth Проверка валидации логина при вводе некорректного кода."""

    page = MainPage(driver)

    page.main_cabinet.click()

    page.find_login.send_keys(abracadabra)  # некорректный код

    page.input_button.click()

    assert page.login_error_message.get_text() == "Найдем вас в Лабиринте или зарегистрируем"


@pytest.mark.negative
def test_login_input_of_an_incorrect_phone_number(driver):
    """ 05 auth Проверка ввода некорректного номера телефона."""

    page = MainPage(driver)

    page.main_cabinet.click()

    page.find_login.send_keys('9999999999')  # некорректный номера телефона

    page.input_button.click()

    assert page.login_error_message.get_text() == "Найдем вас в Лабиринте или зарегистрируем"



