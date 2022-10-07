import os

from pages.web_page import WebPage
from pages.web_element import WebElement
from pages.web_element import ManyWebElements
from settings import *
from pages.search_result_page import SearchResultPage


class MainPage(WebPage):
    def __init__(self, driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or main_url
        super().__init__(driver, url)

    # шапка страницы
    logo = WebElement(WebPage, xpath='//a[@class="b-header-b-logo-e-logo-wrap"]')  # логотип + ссылка на главную стр.
    main_cabinet = WebElement(WebPage, css_selector='.top-link-main_cabinet')  # кнопка "Мой Лаб"
    user_name = WebElement(WebPage, css_selector='span.js-b-autofade-text')  # имя пользователя в шапке страницы
    search_field = WebElement(WebPage, id='search-field')  # поле поиска
    search_button = WebElement(WebPage, css_selector='button.b-header-b-search-e-btn')  # кнопка Искать
    # кнопка Отложено
    postponed_mp = \
        WebElement(WebPage, xpath='//a[@class="b-header-b-personal-e-link top-link-main top-link-main_putorder"]')
    # количество отложенных товаров
    postponed_counter_mp = WebElement\
        (WebPage, css_selector='div.top-header span.b-header-b-personal-e-icon-count-m-putorder.basket-in-dreambox-a')
    cart = WebElement(WebPage, css_selector='.top-header a[href="/cart/"]')  # кнопка Корзина
    # количество товаров в корзине
    cart_counter = WebElement\
        (WebPage, css_selector='div.top-header span.b-header-b-personal-e-icon-count-m-cart.basket-in-cart-a')
    support_link = WebElement\
        (WebPage, css_selector='li.b-header-b-sec-menu-e-list-item.analytics-click-js', link_text='Поддержка')
    products_titles = WebElement(WebPage, xpath='//a[@class="b-header-b-logo-e-logo"]')  # товаров на странице

    # подвал страницы
    vk_link = WebElement(WebPage, css_selector='div.b-rfooter-links-content a', link_text='ВКонтакте')
    all_books = WebElement(WebPage, css_selector='div.b-rfooter-links-content a', link_text='Все книги')

    # модальная страница для авторизации
    find_login = WebElement(WebPage, css_selector='.full-input__input.formvalidate-error')  # поле для ввода логина
    login_error_message = WebElement(WebPage, css_selector='form#auth-by-code small.full-input__msg-small.js-msg-small')
    input_button = WebElement(WebPage, id='g-recap-0-btn')  # Войти
    # Другие способы входа
    other_ways_to_login = WebElement(WebPage, xpath='//a[@class="js-show-soc analytics-click-js"]')
    mail_login_button = WebElement(WebPage, css_selector='a[title="Mail.ru"]')  # Mail.ru

    # модальная страница успешной авторизации
    success_login = WebElement(WebPage, css_selector='form#auth-success-login div.js-auth__title.new-auth__title')

    # элементы страницы для авторизации
    my_mail_login_input = WebElement(WebPage, xpath='//input[@name="username"]')  # ввода логина
    my_mail_enter_button = WebElement(WebPage, xpath='//*[@class="inner-0-2-89 innerTextWrapper-0-2-90"]')  # Войти
    my_mail_password_input = WebElement(WebPage, xpath='//*[@name="password"]')  # ввод пароля
    allow_my_mail_button = WebElement(WebPage, xpath='//button[@data-test-id="accept-access"][@type="button"]')  # Войти

    # модальное окно при добавлении книги в Отложено
    add_to_favorite_popup = WebElement\
        (WebPage, css_selector='div.b-basket-popinfo-e-text.b-basket-popinfo-e-text-m-add.b-basket-popinfo-e-text-m-gray')

    # модальное окно при добавлении книги в Корзину
    add_to_cart_popup = WebElement\
        (WebPage, css_selector='div.b-basket-popinfo-e-text.b-basket-popinfo-e-text-m-add.b-basket-popinfo-e-text-m-gray')

    # модальное окно с кнопкой "Принять"
    accept_cookie = WebElement(WebPage, css_selector='button.cookie-policy__button.js-cookie-policy-agree')

    # элементы на главной странице

    # троеточие под первой книгой
    open_actions_block = WebElement(WebPage, css_selector='a.icon-compare.track-tooltip.js-open-actions-block')
    # кнопка добавить в избранное
    add_to_compare = WebElement(WebPage, css_selector='a.b-list-item-hover.js-card-block-actions-compare')
    # поле для ввода email, по которому можно получить купон
    #input_email = WebElement(WebPage, css_selector='input.getemail-form-input.js-getemail')
    input_email = WebElement(WebPage, xpath=
    '//*[@style="font-family: Roboto-bold,Helvetica,Arial,sans-serif!important; font-size: 15px; font-weight: bold;"]')

    get_coupon_button = WebElement(WebPage, css_selector='div.getemail-main-left-btn-outer')  # кнопка "Получить купон"
    used_email_text = WebElement(WebPage, css_selector='label.getemail-form-label.getemail-form-e-text')
    # кнопка "В корзину" у первого товара
    add_to_cart = WebElement(WebPage, css_selector='div.product-buy.buy-avaliable.fleft a.btn.buy-link.btn-primary')

    # элементы меню на главной странице
    # Книги
    menu_button_books = WebElement(WebPage, xpath='//*[@class="b-header-b-menu-e-link top-link-menu first-child"]')
    # Главное 2022
    menu_button_Main_2022 = WebElement\
        (WebPage, xpath='//a[@class="b-header-b-menu-e-text"][contains(text(),"Главное 2022")]')
    # Школа
    menu_button_school = WebElement(WebPage, xpath='//a[@href="/school/"][contains(text(),"Школа")]')
    # Игрушки
    menu_button_games = WebElement(WebPage, xpath='//a[@class="b-header-b-menu-e-text"][contains(text(),"Игрушки")]')
    # Канцтовары
    menu_button_stationery = WebElement(WebPage, xpath=
    '//a[@class="b-header-b-menu-e-text"][contains(text(),"Канцтовары")]')
    # Ещё
    menu_button_more = WebElement(WebPage, xpath=
    '//span[@class="b-header-b-menu-e-link top-link-main have-dropdown-touchlink"]')
    # CD/DVD
    menu_button_CD_DVD = WebElement(WebPage, xpath=
    '//a[@href="/multimedia/"][@title="Аудиокниги, музыка, видеофильмы, компьютерные программы, игры и др."]')
    # Сувениры
    menu_button_souvenir = WebElement(WebPage, xpath=
    '//a[@href="/souvenir/"][@title="Сувениры, альбомы для фотографий, фоторамки, календари."]')
    # Журналы
    menu_button_journals = WebElement(WebPage, xpath=
    '//a[@href="/journals/"][@title="Литературные журналы: художественные и публицистические, поэтические."]')
    # Товары для дома
    household_goods = WebElement(WebPage, xpath='//a[@href="/household/"][@title="Товары для дома"]')
    # Клуб
    button_club = WebElement(WebPage, xpath='//a[@class="b-header-b-menu-e-text"][contains(text(),"Клуб")]')
    # Регион
    region_location = WebElement(WebPage, xpath='//span[@class="region-location-icon-txt "]')
    # поле ввода региона
    input_region_location = WebElement(WebPage, id="region-post")
    # Значок меню Пункты самовывоза
    pick_up_points = WebElement(WebPage, xpath='//*[@href="/maps/"][@class="b-header-b-sec-menu-e-link"]')
    # Значок меню Доставка и оплата
    delivery_and_payment = WebElement(WebPage, xpath='//a[@href="/help/"][contains(text(),"Доставка и оплата")]')
    # Значок меню  В соцсетях
    social_networks = WebElement(WebPage, xpath='//*[@title="Лабиринт в соцсетях"]')
      # Значок в выпадающем списке меню  В контакте
    icon_v_kontakte = WebElement(WebPage, xpath='//a[@href="https://vk.com/labirintru"][@data-event-label="vk"]')
    # названия товаров в результатах поиска
    product_titles = ManyWebElements(WebPage, xpath='//*[@class="product need-watch watched"]')

    successful_search = WebElement(WebPage, xpath='//span[contains(text(),"Все, что мы нашли в Лабиринте по запросу")]')
    not_successful_search = WebElement(
        WebPage, xpath='//h1[contains(text(),"Мы ничего не нашли по вашему запросу! Что делать?")]')

    # все фильтры
    all_filers = WebElement(WebPage, xpath='//span[contains(text(), "ВСЕ ФИЛЬТРЫ") and @class="navisort-item__content"]')
    # сбросить
    reset_all_filers = WebElement(WebPage, xpath='//*[@id="rubric-tab"]/div[2]/div[1]/div/div[2]/div/span[3]')
    # радиокнопка  В наличии
    available = WebElement(WebPage, xpath='//*[@id="section-search-form"]/div[2]/div[2]/div[1]/label[1]/span[2]')
    # нет в продаже
    not_available = WebElement(WebPage, xpath='//*[@id="section-search-form"]/div[2]/div[2]/div[4]/label[1]/span[2]')
    # Показать
    show_all_found = WebElement(WebPage, xpath='//input[@class="show-goods__button"]')

    search_result_goods = WebElement(WebPage, xpath='//a[@class="show-goods__button"]')
    search_results_count = ManyWebElements(
        WebPage, xpath='//*[@class="b-stab-e-slider-item-e-txt-m-small js-search-tab-count"]')
    search_result_genres = WebElement(WebPage, xpath='//*[@id="stab-slider-frame"]/ul/li[2]')
    search_result_theme = WebElement(WebPage, xpath='//*[@id="stab-slider-frame"]/ul/li[3]')

    # модальное окно при получении купона
    received_coupon_popup = WebElement(WebPage, xpath='//*[@id="stab-slider-frame"]/ul/li[1]/a/span[1]')

    def get_email_is_in_use_text(self):
        print(self.used_email_text.get_text())
        return self.used_email_text.get_text()

    def get_first_book_by_name(self, book_name):  # первая найденная книга по названию
        self.search_field.wait_to_be_clickable()
        self.search_field.send_keys(book_name)

        self.search_button.wait_to_be_clickable()
        self.search_button.click()
        self.wait_page_loaded()
        search_url = self.get_current_url()
        search_result_page = SearchResultPage(self._web_driver, search_url)
        search_result_page.book_name.wait_to_be_clickable()
        first_book_name = search_result_page.book_name
        first_book_author = search_result_page.book_author

        return first_book_name, first_book_author, search_result_page.add_to_favorite, search_result_page.add_to_cart

