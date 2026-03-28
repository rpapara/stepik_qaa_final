
import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption(
        "--language",
        action="store",
        default="en",
        help="Choose default user language for browswer, ex.: en, ru",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        help="Run browser in headless mode",
    )


@pytest.fixture(scope="function")
def browser(request):
    user_language = request.config.getoption("language")
    headless = request.config.getoption("--headless")
    print(f"\nstart browser for language {user_language} \n")
    options = webdriver.ChromeOptions()

    if headless:
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")
        
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.quit()
