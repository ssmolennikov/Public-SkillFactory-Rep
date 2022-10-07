from pages.web_page import WebPage
from pages.web_element import WebElement
from settings import checkout_page


# страница "Корзина"
class CheckoutPage(WebPage):
    def __init__(self, driver, url=''):
        if not url:
            url = checkout_page
        super().__init__(driver, url)


    # заголовок стрницы "Оформление заказа"
    page_title = WebElement(WebPage, css_selector='div.checkout__header h1')