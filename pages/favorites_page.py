from pages.web_page import WebPage
from pages.web_element import WebElement
from settings import favorites_url


# страница Отложено
class FavoritesPage(WebPage):
    def __init__(self, driver, url=''):
        if not url:
            url = favorites_url
        super().__init__(driver, url)


    select_all_postponded = WebElement(WebPage, xpath="//button[contains(text(),'Выбрать все')]")  # выбрать все
    # clear_favorite = WebElement(WebPage, link_text='Очистить')  # кнопка "Очистить"
    clear_favorite = WebElement(WebPage, xpath="//a[contains(text(),'Удалить')]")  # кнопка "Очистить"
    message = WebElement(WebPage,
                         css_selector='div#messages-text p.g-alttext-small')  # сообщение "Выбранные товары удалены"
    no_favorite_goods = WebElement(WebPage, id='cabinet')  # текст на случай если нет отложенных товаров
    # модальное окно с кнопкой "Принять"
    accept_cookie = WebElement(WebPage, css_selector='button.cookie-policy__button.js-cookie-policy-agree')
    # количество отложено
    postponed_counter_fp = WebElement\
        (WebPage, css_selector='div.top-header span.b-header-b-personal-e-icon-count-m-putorder.basket-in-dreambox-a')
    #postponed_fp = WebElement(WebPage, link_text='Отложено')  # кнопка Отложено
    postponed_fp = WebElement(WebPage,
                              xpath='//a[@class="b-header-b-personal-e-link top-link-main top-link-main_putorder"]')
    # количество отложенных товаров
    postponed_counter1 = WebElement\
        (WebPage, xpath='//*[@class="b-header-b-personal-e-icon-count-m-putorder basket-in-dreambox-a hidden-force"]')