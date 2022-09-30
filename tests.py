import pytest
from selenium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(autouse=True)
def testing():
    pytest.driver = webdriver.Chrome("./drivers/chromedriver")
    # Переходим на страницу авторизации
    pytest.driver.get('http://petfriends1.herokuapp.com/login')

    yield

    pytest.driver.quit()


def test_show_my_pets():
    # неявное ожидание 5 сек. при каждом шаге
    pytest.driver.implicitly_wait(5)

    # Вводим email
    pytest.driver.find_element_by_id('email').send_keys('sssmolennikov@mail.ru')
    # Вводим пароль
    pytest.driver.find_element_by_id('pass').send_keys('Horse2011')

    # Нажимаем на кнопку входа в аккаунт
    pytest.driver.find_element_by_css_selector('button[type="submit"]').click()

    # Проверяем, что мы оказались на главной странице
    assert pytest.driver.find_element_by_tag_name('h1').text == "PetFriends"
    # Нажимаем на кнопку перехода к выбору списка питомцев
    pytest.driver.find_element_by_xpath('//button[@class="navbar-toggler"]').click()

    # Нажимаем на кнопку для перехода к списку своих питомцев
    pytest.driver.find_element_by_xpath('//a[@href="/my_pets"]').click()

    # явное ожидание 10 сек.
    WebDriverWait(pytest.driver, 10).until(EC.presence_of_element_located((By.ID, 'all_my_pets')))

    # Проверяем, что мы оказались на странице со списком своих питомцев
    assert pytest.driver.find_element_by_tag_name('h2').text == "basik"

    # объявляем 4 переменные, в которых записываем все найденные элементы на странице:
    # в images — все картинки питомцев,
    # в names — все их имена,
    # в breeds — все породы животных,
    # в years - все возрасты
    images = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]//img')
    names = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/td[1]')
    breeds = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/td[2]')
    years = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr/td[3]')

    # объявляем переменную, в которую записываем текстовое значение элемента на странице,
    # в котором содержится информация об общем количестве питомцев пользователя
    my_pets = pytest.driver.find_element_by_xpath('/html/body/div[1]/div/div[1]').text
    # строку преобразуем в список
    list_my_pets = my_pets.split()

    # Проверяем, что на странице присутствуют все питомцы пользователя
    # общее количество питомцев пользователя равно длине списка имен
    assert int(list_my_pets[2]) == len(names)

    images1 = []
    for i in range(len(images)):
        if images[i].get_attribute('src') != '':
            images1.append(images[i])

    # Проверяем, что хотя бы у половины питомцев есть фото
    assert len(images1) >= int(list_my_pets[2]) / 2

    # Создаем пустой список, в который будем добавлять текстовые значения имен питомцев
    names1 = []
    # Создаем список, в который будем добавлять непустые значения имен питомцев
    names2 = []
    # Проходимся по списку names, добавляем в список names1 все текстовые значения имен питомцев
    for i in range(len(names)):
        names1.append(names[i].text)
        # проверяем, если текстовое значение элемента не пустое, то добавляем его в список names2
        if names[i].text != '':
            names2.append(names[i].text)

    # Создаем пустой список, в который будем добавлять текстовые значения пород питомцев
    breeds1 = []
    # Создаем список, в который будем добавлять непустые значения пород питомцев
    breeds2 = []
    # Проходимся по списку breeds, добавляем в список breeds1 все текстовые значения пород питомцев
    for i in range(len(breeds)):
        breeds1.append(breeds[i].text)
        # проверяем, если текстовое значение элемента не пустое, то добавляем его в список breeds2
        if breeds[i].text != '':
            breeds2.append(breeds[i].text)

    # Создаем пустой список, в который будем добавлять текстовые значения возрастов питомцев
    years1 = []
    # Создаем список, в который будем добавлять непустые значения возрастов питомцев
    years2 = []
    # Проходимся по списку years, добавляем в список years1 все текстовые значения возрастов питомцев
    for i in range(len(years)):
        years1.append(years[i].text)
        # проверяем, если текстовое значение элемента не пустое, то добавляем его в список years2
        if breeds[i].text != '':
            years2.append(years[i].text)

    # Проверяем, что у всех питомцев есть имя, возраст и порода
    assert int(list_my_pets[2]) == len(breeds2) and int(list_my_pets[2]) == len(names2) and int(
        list_my_pets[2]) == len(years2)

    # Создаем пустой список, в который будем добавлять повторяющиеся имена питомцев
    names3 = []
    # Проходимся по списку текстовых значений names1 и добавляем повторяющиеся его элементы в список names3
    for n in range(len(names1)):
        for j in range(n + 1, len(names1)):
            if names1[n] == names1[j]:
                names3.append(names1[n])

    # Проверяем, что у всех питомцев разные имена, список names3 должен быть пустой
    assert len(names3) == 0

    # объявляем переменную, в которую записываем все найденные элементы на странице (вся инфомация в карточках питомцев)
    pets = pytest.driver.find_elements_by_xpath('//*[@id="all_my_pets"]/table/tbody/tr')
    # создаем 2 пустых списка
    pets1 = []
    pets2 = []
    # Проходим по списку pets и добавляем в список pets1 текстовые значения элементов
    for i in range(len(pets)):
        pets1.append(pets[i].text)

    # Проходим по списку pets1 и добавляем в список pets повторяющиеся элементы
    for n in range(len(pets1)):
        for j in range(n + 1, len(pets1)):
            if pets1[n] == pets1[j]:
                pets2.append(pets1[n])

    assert len(pets2) == 0
