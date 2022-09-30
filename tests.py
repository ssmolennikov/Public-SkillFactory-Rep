import pytest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from link import *


@pytest.fixture(autouse=True)
def testing():
    """Chrome Driver"""
    pytest.driver = webdriver.Chrome(executable_path=DRIVER_PATH)
    # Неявное ожидание
    pytest.driver.implicitly_wait(5)
    # Переходим на страницу авторизации
    pytest.driver.get(pet_friends_login)

    yield

    pytest.driver.quit()


def test_all_pets():
    # Auth on website
    # Entering email
    pytest.driver.implicitly_wait(10)
    pytest.driver.find_element(By.ID, 'email').send_keys(valid_email)
    # Entering Password
    pytest.driver.find_element(By.ID, 'pass').send_keys(valid_password)
    # Press on the button to enter into account
    pytest.driver.find_element(By.CSS_SELECTOR, btn_click).click()
    # Check that we are on the user home page
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    pytest.driver.implicitly_wait(10)
    images = pytest.driver.find_elements(By.CSS_SELECTOR, all_card_deck_image)
    names = pytest.driver.find_elements(By.CSS_SELECTOR, all_card_deck_names)
    descriptions = pytest.driver.find_elements(By.CSS_SELECTOR, all_card_deck_descriptions)

    for i in range(len(names)):
        name = names[i].text
        image = images[i].get_attribute('src')
        desc = descriptions[i].text
        assert image != '' and image != '(unknown)'
        assert name != ''
        assert desc != '' and desc != 'None, None лет'
        assert ',' in desc
        parts = desc.split(",")
        assert len(parts[0]) > 0 and parts[0] != 'None'
        assert len(parts[1]) > 0 and parts[1] != 'None лет' and parts[1] != ' лет'


def test_my_pets():
    wait = WebDriverWait(pytest.driver, 5)
    # Auth on website
    # Entering email
    wait.until(EC.presence_of_element_located((By.ID, "email"))).send_keys(valid_email)

    # Entering password
    wait.until(EC.presence_of_element_located((By.ID, "pass"))).send_keys(valid_password)

    # Press on the button to enter into account
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, btn_click))).click()

    # Check that we are on the user home page
    assert pytest.driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"

    # Go to the page of your pets
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, my_pets))).click()
    assert pytest.driver.find_element(By.TAG_NAME, 'h2').text == "sssmolennikov"

    # number of pets
    # save the statistics elements to the data_stats variable
    data_stats = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, profile_statistics)))

    # Getting the number of pets from statistics data
    statistic = data_stats[0].text.split('\n')
    statistic = statistic[1].split(' ')
    statistic = int(statistic[1])
    assert statistic > 0

    # Checking that the number of rows in the table is equal to the number recorded in the statistics
    images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'IMG')))
    count_table = len(images) - 1
    assert count_table >= 0
    assert statistic == count_table

    # Using the counter to count the number of user's pets with a photo
    pytest.driver.implicitly_wait(5)
    photo_presence = 0

    # determine the number of pets with a photo by a non-empty value of the scr attribute
    for i in range(count_table):
        photo = images[i].get_attribute('src')
        if photo != '' and photo != '(unknown)':
            photo_presence += 1
        else:
            photo_presence = photo_presence

    # Checking that at least half of all pets have a photo
    assert photo_presence >= (count_table // 2)

    # Check that pets have all the data filled in: name, type, age
    my_list = []
    my_names = []

    # constant part in Xpath
    x_path = CONSTANT_XPATH
    for i in range(1, count_table + 1):
        line = ''
        pytest.driver.implicitly_wait(5)
        name = pytest.driver.find_element(By.XPATH, x_path + str(i) + "]/td[1]").text
        assert name != '', 'У питомца отсутствует имя'
        line += name
        my_names.append(line)
        tip = pytest.driver.find_element(By.XPATH, x_path + str(i) + "]/td[2]").text
        assert tip != '' and tip != 'None'
        line += tip
        age = pytest.driver.find_element(By.XPATH, x_path + str(i) + "]/td[3]").text
        assert age != '' and age != 'None лет' and age != ' лет'
        line += age
        my_list.append(line)
    assert my_list != []
    assert my_names != []

    # Check that the list does not contain duplicate information about pets (name, breed, age)
    my_set = set(my_list)
    assert len(my_set) == count_table

    # Checking that there are no duplicate pet names in the list
    my_set_names = set(my_names)
    assert len(my_set_names) == count_table
