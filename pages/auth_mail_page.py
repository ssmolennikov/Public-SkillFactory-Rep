from pages.web_page import WebPage


# страница просмотра книги
class AboutBookPage(WebPage):
    def __init__(self, driver, url):
        super().__init__(driver, url)

