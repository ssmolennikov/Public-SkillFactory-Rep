from pages.web_page import WebPage
from pages.web_element import WebElement
from settings import compare_url


# страница "Корзина"
class ComparetPage(WebPage):
    def __init__(self, driver, url=''):
        if not url:
            url = compare_url
        super().__init__(driver, url)


    # кнопка удаления сравнительного списка книг
    delete_compare_list_button = WebElement(WebPage, css_selector='div.compare-delete-list')

    # текст на старнице когда нет товаров для сравнения
    empty_compare_text = WebElement(WebPage, css_selector='p.compare-text-empty')