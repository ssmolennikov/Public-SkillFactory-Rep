import time
import pytest

from pages.main_page import MainPage
from pages.about_book_page import AboutBookPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from settings import *
from selenium.webdriver.common.action_chains import ActionChains


def generate_string(num):
    return "x" * num

def russian_chars():
    return 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def chinese_chars():
    return '的一是不了人我在有他这为之大来以个中上们'

def special_chars():
    return '|\\/!@#$%^&*()-_=+`~?"№;:[]{}'


@pytest.mark.positive
def test_absence_of_goods_in_the_basket(driver):
    """ 01 c Проверка отсутствие товаров в корзине."""

    page = MainPage(driver)
    page.cart.wait_to_be_clickable()
    page.cart.click()
    page.wait_page_loaded()
    cart_page = CartPage(driver, page.get_current_url())
    cart_page.empty_cart_text.wait_to_be_clickable()

    assert 'ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?' in cart_page.empty_cart_text.get_text()


@pytest.mark.positive
def test_transition_from_the_shopping_cart_page_to_the_main_page(driver):
    """ 02 c Проверка перехода со страницы "Корзина" на главную."""

    page = MainPage(driver)
    page.cart.click()
    page.logo.wait_to_be_clickable()
    page.logo.click()

    assert page.get_current_url() == main_url


@pytest.mark.positive
def test_addition_of_the_first_found_book_to_the_cart(driver):
    """ 03 c Проверка добавления в корзину первой найденной книги."""

    page = MainPage(driver)

    _, _, _, add_to_cart = page.get_first_book_by_name(author_book)
    add_to_cart.click()
    page.add_to_cart_popup.wait_to_be_clickable()

    # проверка появления сообщение об успешном добавлении в корзину
    assert 'Вы добавили в корзину книгу' in page.add_to_cart_popup.get_text()

    page.cart_counter.wait_to_be_clickable()
    cart_counter = int(page.cart_counter.get_text())

    # проверка увеличения счетчик товаров в корзине
    assert cart_counter > 0


@pytest.mark.positive
def test_adding_to_the_cart_from_the_book_view_page(driver):
    """ 04 c Проверка добавления в корзину со страницы просмотра книги."""

    page = MainPage(driver)
    page.accept_cookie.click()
    name_found_book, _, _, add_to_cart = page.get_first_book_by_name(author_book)
    name_found_book.click()
    page.wait_page_loaded()
    about_book_page = AboutBookPage(driver, page.get_current_url())
    about_book_page.add_to_cart.wait_to_be_clickable()
    about_book_page.add_to_cart.click()

    # проверяем, что название кнопки изменилось
    assert about_book_page.add_to_cart.get_text() == 'Оформить заказ'

    page.cart_counter.wait_to_be_clickable()

    cart_counter = int(page.cart_counter.get_text())

    # проверяем, что счетчик увеличился
    assert cart_counter > 0

    page.add_to_cart_popup.wait_to_be_clickable()

    assert 'Вы добавили в корзину книгу' in page.add_to_cart_popup.get_text()


@pytest.mark.positive
def test_the_purchase_order(driver):
    """ 05 c Проверка оформления покупки."""

    page = MainPage(driver)
    page.accept_cookie.click()
    page.add_to_cart.click()
    page.wait_page_loaded()
    page.cart.click()
    cart_page = CartPage(driver, page.get_current_url())
    cart_page.wait_page_loaded()
    cart_page.go_to_checkout_button.click()
    cart_page.wait_page_loaded()
    checkout_page = CheckoutPage(driver, page.get_current_url())
    checkout_page.wait_page_loaded()

    assert 'Оформление заказа' in checkout_page.page_title.get_text()


@pytest.mark.positive
def test_the_cleaning_of_the_trash(driver):
    """ 06 c Проверка очистки корзины."""

    page = MainPage(driver)
    page.accept_cookie.click()
    page.add_to_cart.click()
    page.wait_page_loaded()
    page.cart.click()
    cart_page = CartPage(driver, page.get_current_url())
    cart_page.wait_page_loaded()
    cart_page.empty_cart_button.click()
    cart_page.wait_page_loaded()

    # проверка появления сообщение 'ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?' после нажатия на "Очистить корзину"
    assert 'ВАША КОРЗИНА ПУСТА. ПОЧЕМУ?' in cart_page.empty_cart_text.get_text()

@pytest.mark.positive
def test_addition_of_the_quantity_of_goods_in_the_cart(driver):
    """ 07 c Проверка добавления количества товара в корзине."""

    page = MainPage(driver)

    _, _, _, add_to_cart = page.get_first_book_by_name(author_book)  # nov
    add_to_cart.click()  # nov
    page.add_to_cart_popup.wait_to_be_clickable()  # nov

    page.accept_cookie.click()  # принимаем куки
    page.add_to_cart.click()  # модальное окно при добавлении книги в Корзину
    page.wait_page_loaded()
    page.cart.click()  # кнопка Корзина

    cart_page = CartPage(driver, page.get_current_url())
    cart_page.wait_page_loaded()

    cart_page.item_increase_button.click()  # кнопка плюс (добавление товара)
    cart_page.wait_page_loaded()

    goods_quantity = int(cart_page.goods_quantity_input.get_attribute('value'))  #

    # Проверка увеличеня товара +1 = 2
    assert goods_quantity == 2


@pytest.mark.positive
def test_addition_and_reduction_of_the_quantity_of_goods_in_the_basket(driver):
    """ 08 c Проверка добавления и уменьшения количества товара в корзине."""

    page = MainPage(driver)
    page.accept_cookie.click()  # принимаем куки
    page.add_to_cart.click()
    page.wait_page_loaded()
    page.cart.click()
    cart_page = CartPage(driver, page.get_current_url())
    cart_page.wait_page_loaded()
    cart_page.item_increase_button.click()
    cart_page.wait_page_loaded()
    cart_page.item_reduction_button.click()
    cart_page.wait_page_loaded()
    goods_quantity = int(cart_page.goods_quantity_input.get_attribute('value'))

    assert goods_quantity == 1


@pytest.mark.xfail
@pytest.mark.negative
@pytest.mark.parametrize("empty_value", ['', ' '], ids=['empty', 'space'])
def test_purchase_registration_with_the_input_of_empty_values_with_the_first_and_last_name(driver, empty_value):
    """ 09 c Проверка оформления покупки с вводом пустых значений в поля с именем и фамилией."""

    page = MainPage(driver)
    page.accept_cookie.click()  # # принимаем куки
    page.add_to_cart.click()  # модальное окно при добавлении книги в Корзину
    page.cart.wait_to_be_clickable()  # ожидаем
    page.cart.click()  # кнопка Корзина

    cart_page = CartPage(driver, page.get_current_url())
    cart_page.go_to_checkout_buttont.wait_to_be_clickable()  # кнопка "Перейти к оформлению"

    cart_page.go_to_checkout_buttont.click()  # кнопка "Перейти к оформлению"
    cart_page.wait_page_loaded()  # ожидаем
    time.sleep(1)  # в учебных целях
    cart_page.name_input.send_keys(empty_value)  # ввод имя
    cart_page.surname_input.send_keys(empty_value)  # ввод фамилия

    cart_page.checkout_button.wait_to_be_clickable()  #
    cart_page.checkout_button.click()

    assert 'Имя обязательно' in cart_page.text_under_name_input.get_text()
    assert 'Фамилия обязательна' in cart_page.text_under_surname_input.get_text()


@pytest.mark.xfail
@pytest.mark.negative
@pytest.mark.parametrize("invalid_value", ['1', special_chars(), chinese_chars()],
                         ids=['number', 'special_chars', 'chinese_chars'])
def test_purchase_registration_with_the_input_of_invalid_values_with_the_first_and_last_name(driver, invalid_value):
    """ 10 c Проверка оформления покупки с вводом невалидных значений в поля с именем и фамилией."""

    page = MainPage(driver)
    page.accept_cookie.click()
    page.add_to_cart.click()
    page.cart.wait_to_be_clickable()
    page.cart.click()

    cart_page = CartPage(driver, page.get_current_url())
    cart_page.go_to_checkout_buttont.wait_to_be_clickable()

    cart_page.go_to_checkout_buttont.click()
    cart_page.wait_page_loaded()
    time.sleep(1)  # в учебных целях
    cart_page.name_input.send_keys(invalid_value)

    cart_page.surname_input.send_keys(invalid_value)
    cart_page.checkout_button.wait_to_be_clickable()
    cart_page.checkout_button.click()

    assert 'Разрешены только буквы' in cart_page.text_under_name_input.get_text()
    assert 'Разрешены только буквы' in cart_page.text_under_surname_input.get_text()


@pytest.mark.xfail
@pytest.mark.negative
def test_purchase_registration_with_the_input_of_large_letter_values_with_the_first_and_last_name(driver):
    """ 11 c Проверка оформления покупки с вводом больших буквенных значений в поля с именем и фамилией."""

    long_text = generate_string(100)
    page = MainPage(driver)

    page.accept_cookie.click()
    page.add_to_cart.click()
    page.cart.wait_to_be_clickable()
    page.cart.click()

    cart_page = CartPage(driver, page.get_current_url())
    cart_page.go_to_checkout_buttont.wait_to_be_clickable()

    cart_page.go_to_checkout_buttont.click()
    cart_page.wait_page_loaded()

    cart_page.name_input.send_keys(long_text)
    cart_page.surname_input.send_keys(long_text)

    cart_page.checkout_button.wait_to_be_clickable()
    cart_page.checkout_button.click()

    assert 'Можно указать не более 50 символов' in cart_page.text_under_name_input.get_text()
    assert 'Можно указать не более 50 символов' in cart_page.text_under_surname_input.get_text()


@pytest.mark.xfail
@pytest.mark.positive
def test_input_valid_phone_number(driver):
    """ 12 c Проверка ввода валидного телефона."""

    phone = valid_phone
    page = MainPage(driver)
    page.accept_cookie.click()
    page.add_to_cart.click()
    page.cart.wait_to_be_clickable()
    page.cart.click()
    cart_page = CartPage(driver, page.get_current_url())
    cart_page.go_to_checkout_buttont.wait_to_be_clickable()
    cart_page.go_to_checkout_buttont.click()
    cart_page.wait_page_loaded()
    cart_page.phone_input.scroll_to_element()
    cart_page.phone_input.wait_to_be_clickable()

    element = cart_page.get_phone_input(driver)
    actions = ActionChains(driver)
    actions.move_to_element(element).send_keys(phone).perform()

    cart_page.checkout_button.wait_to_be_clickable()
    cart_page.checkout_button.click()

    assert 'Этот телефон уже есть в Лабиринте' in cart_page.text_under_phone_input.get_text()


@pytest.mark.xfail
@pytest.mark.parametrize("invalid_phone", ['111', '+7111111111111', '++++++++', '----------', '()'],
                         ids=['short_num', 'long_num', 'pluses', 'minuses', 'brackets'])
@pytest.mark.negative
def test_input_invalid_phone_number(driver, invalid_phone):
    """ 13 c Проверка ввода невалидного телефона."""

    phone = invalid_phone
    page = MainPage(driver)
    page.accept_cookie.click()
    page.add_to_cart.click()
    page.cart.wait_to_be_clickable()
    page.cart.click()
    cart_page = CartPage(driver, page.get_current_url())
    cart_page.go_to_checkout_buttont.wait_to_be_clickable()
    cart_page.go_to_checkout_buttont.click()
    cart_page.wait_page_loaded()
    cart_page.phone_input.scroll_to_element()
    cart_page.phone_input.wait_to_be_clickable()

    element = cart_page.get_phone_input(driver)
    actions = ActionChains(driver)
    actions.move_to_element(element).send_keys(phone).perform()

    cart_page.checkout_button.wait_to_be_clickable()
    cart_page.checkout_button.click()

    assert 'Ошибка в номере телефона' in cart_page.text_under_phone_input.get_text()


@pytest.mark.xfail
@pytest.mark.parametrize("invalid_symbols", [' ', 'abc', 'абв'], ids=['space', 'eng_letters', 'ru_letters'])
@pytest.mark.negative
def test_input_invalid_value_in_phone_field(driver, invalid_symbols):
    """ 14 c Проверка ввода невалидного данных в поле для телефона."""

    phone = invalid_symbols
    page = MainPage(driver)
    page.accept_cookie.click()
    page.add_to_cart.click()
    page.cart.wait_to_be_clickable()
    page.cart.click()
    cart_page = CartPage(driver, page.get_current_url())
    cart_page.go_to_checkout_buttont.wait_to_be_clickable()
    cart_page.go_to_checkout_buttont.click()
    cart_page.wait_page_loaded()
    cart_page.phone_input.scroll_to_element()
    cart_page.phone_input.wait_to_be_clickable()

    element = cart_page.get_phone_input(driver)
    actions = ActionChains(driver)
    actions.move_to_element(element).send_keys(phone).perform()

    cart_page.checkout_button.wait_to_be_clickable()
    cart_page.checkout_button.click()

    assert 'Телефон обязателен' in cart_page.text_under_phone_input.get_text()


