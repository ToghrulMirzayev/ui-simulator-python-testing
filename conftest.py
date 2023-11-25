from pytest import fixture
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.index_page import IndexPage
from pages.check_and_validate_page import CheckAndValidatePage
from pages.input_and_click_page import InputAndClickPage
from pages.hover_and_select_page import HoverAndSelectPage
from pages.drag_and_drop_page import DragAndDropPage
from env_setup import URLSetup


@fixture
def get_chrome_options():
    """
    Fixture to handle additional options
    :return: options
    """
    options = ChromeOptions()
    options.add_argument('--headless')
    return options


@fixture
def get_webdriver(get_chrome_options):
    """
    Fixture that will create driver instance that will be reusable across codebase
    :param get_chrome_options: fixture that will contain additional options
    :return: driver instance
    """
    driver = webdriver.Chrome(options=get_chrome_options, service=Service(ChromeDriverManager().install()))
    return driver


@fixture
def index_page(get_webdriver):
    """
    Fixture that will create IndexPage instance
    :param get_webdriver: fixture that will provide driver instance
    :return: IndexPage instance
    """
    get_webdriver.get(URLSetup.INDEX_PAGE_URL)
    yield IndexPage(get_webdriver)
    get_webdriver.quit()


@fixture
def check_and_validate_page(get_webdriver):
    """
    Fixture that will create CheckAndValidatePage instance
    :param get_webdriver: fixture that will provide driver instance
    :return: CheckAndValidatePage instance
    """
    get_webdriver.get(URLSetup.CHECK_AND_VALIDATE_PAGE_URL)
    yield CheckAndValidatePage(get_webdriver)
    get_webdriver.quit()


@fixture
def input_and_click_page(get_webdriver):
    """
    Fixture that will create InputAndClickPage instance
    :param get_webdriver: fixture that will provide driver instance
    :return: InputAndClickPage instance
    """
    get_webdriver.get(URLSetup.INPUT_AND_CLICK_PAGE_URL)
    yield InputAndClickPage(get_webdriver)
    get_webdriver.quit()


@fixture
def hover_and_select_page(get_webdriver):
    """
    Fixture that will create HoverAndSelectPage instance
    :param get_webdriver: fixture that will provide driver instance
    :return: HoverAndSelectPage instance
    """
    get_webdriver.get(URLSetup.HOVER_AND_SELECT_PAGE_URL)
    yield HoverAndSelectPage(get_webdriver)
    get_webdriver.quit()


@fixture
def drag_and_drop_page(get_webdriver):
    """
    Fixture that will create DragAndDropPage instance
    :param get_webdriver: fixture that will provide driver instance
    :return: DragAndDropPage instance
    """
    get_webdriver.get(URLSetup.DRAG_AND_DROP_PAGE_URL)
    yield DragAndDropPage(get_webdriver)
    get_webdriver.quit()
