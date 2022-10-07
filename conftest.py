import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from settings import valid_email, valid_password, main_url


@pytest.fixture(scope='function')
def driver():
    capabilities = DesiredCapabilities().CHROME
    capabilities["pageLoadStrategy"] = "none"

    driver = webdriver.Chrome('../chromedriver', desired_capabilities=capabilities)
    driver.maximize_window()

    yield driver

    # driver.close()
    driver.quit()


@pytest.fixture(scope='function')
def driver_with_cookies(driver):
    response = requests.post(url=f"{main_url}/login", data={"email": valid_email, "pass": valid_password})
    assert response.status_code == 200
    assert 'Cookie' in response.request.headers, 'В запросе не передан ключ авторизации'
    print('\n getting auth_key')
    driver.get(main_url)
    cookie_list = response.request.headers.get('Cookie').split('=')
    driver.add_cookies({'name': cookie_list[0], 'value': cookie_list[1]})
    yield driver


def get_test_case_docstring(item):
    """ This function gets doc string from test case and format it
        to show this docstring instead of the test case name in reports.
    """

    full_name = ''

    if item._obj.__doc__:
        # Remove extra whitespaces from the doc string:
        name = str(item._obj.__doc__.split('.')[0]).strip()
        full_name = ' '.join(name.split())

        # Generate the list of parameters for parametrized test cases:
        if hasattr(item, 'callspec'):
            params = item.callspec.params

            res_keys = sorted([k for k in params])
            # Create List based on Dict:
            res = ['{0}_"{1}"'.format(k, params[k]) for k in res_keys]
            # Add dict with all parameters to the name of test case:
            full_name += ' Parameters ' + str(', '.join(res))
            full_name = full_name.replace(':', '')

    return full_name


def pytest_itemcollected(item):
    """ This function modifies names of test cases "on the fly"
        during the execution of test cases.
    """

    if item._obj.__doc__:
        item._nodeid = get_test_case_docstring(item)


def pytest_collection_finish(session):
    """ This function modified names of test cases "on the fly"
        when we are using --collect-only parameter for pytest
        (to get the full list of all existing test cases).
    """

    if session.config.option.collectonly is True:
        for item in session.items:
            # If test case has a doc string we need to modify it's name to
            # it's doc string to show human-readable reports and to
            # automatically import test cases to test management system.
            if item._obj.__doc__:
                full_name = get_test_case_docstring(item)
                print(full_name)

        pytest.exit('Done!')