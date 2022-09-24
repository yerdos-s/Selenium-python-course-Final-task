import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                     help="Choose browser: chrome or firefox")
    parser.addoption('--language', action = 'store', default = "en",
                     help='Choose language: ru,en-gb,es,pt etc.')


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")
    driver = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        driver = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print("\nquit browser..")
    driver.quit()
