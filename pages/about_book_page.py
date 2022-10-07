from pages.web_page import WebPage
from pages.web_element import WebElement


# страница просмотра информации о книге
class AboutBookPage(WebPage):
    def __init__(self, driver, url):
        super().__init__(driver, url)


    # номер isbn книги
    isbn = WebElement(WebPage, css_selector='div.isbn')

    # кнопка "Добавить в корзину"
    add_to_cart = WebElement(WebPage, css_selector='a#buyto-buyids')