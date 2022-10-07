from pages.web_page import WebPage
from pages.web_element import WebElement


# страница просмотра информации об авторе
class AboutAuthorPage(WebPage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

    author_name = WebElement(WebPage, css_selector='div.content-default.read-area h1') # ФИО автора в заголовке