from pages.web_page import WebPage
from pages.web_element import WebElement


class SearchResultPage(WebPage):  # Страница результатов поиска
    def __init__(self, driver, url):
        super().__init__(driver, url)

    # страница с результатами поиска (по умолчанию вкладка "Товары")
    authors_link = WebElement(WebPage, css_selector='a[data-id_tab="1"]')  # вкладка "Авторы"
    found_author = WebElement(WebPage, css_selector='a.rubric-list-item')  # первый автор в списке результатов
    search_result = WebElement(WebPage, xpath='//span[@class="rubric-item-name"]')  # первый автор в списке результатов

    book_name = WebElement(WebPage, css_selector='span.product-title')  # имя первого найденного товара (название книги)
    # имя автора первого найденного товара (автор книги)
    book_author = WebElement(WebPage, css_selector='div.product-author > a > span')
    # кнопка "Отложить" у первого товара
    add_to_favorite = WebElement(WebPage, css_selector='.icon-fave.track-tooltip.js-open-deferred-block')
    delete_from_favorite = \
        WebElement(WebPage, css_selector='div.js-putorder-block-change.b-dropdown-window span.b-list-item-hover.pointer')
    # кнопка "В корзину" у первого товара
    add_to_cart = WebElement(WebPage, css_selector='div.product-buy.buy-avaliable.fleft a.btn.buy-link.btn-primary')

    # страница с ненайденным результатом поиска
    # строка с сообщениемм 'Мы ничего не нашли по вашему запросу! Что делать?'
    not_found_issue = WebElement(WebPage, css_selector='div.search-error h1')

    enter_something = WebElement(WebPage, xpath='//input[@type="text"][@tabindex="11"]')  # введеное слово (комиксы)

