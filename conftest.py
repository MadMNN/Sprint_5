import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()  # Открытие окна на весь экран
    yield driver
    driver.quit()
