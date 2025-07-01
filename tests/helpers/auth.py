from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from tests.helpers.urls import *
import random
import string

# helpers/auth.py


def login(driver, email, password):
    driver.get(MAIN_PAGE_URL)

    driver.find_element(By.XPATH, "//button[contains(text(), 'Вход и регистрация')]").click()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Введите Email']"))
    ).send_keys(email)

    driver.find_element(By.XPATH, "//input[@placeholder='Пароль']").send_keys(password)
    driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()

    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//div[contains(@class, 'columnSmall') and contains(text(), 'User')]"))
    )


# Генерация уникального email

def generate_unique_email(domain='example.com'):
    """Генерирует уникальный email для регистрации."""
    prefix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=10))
    return f"{prefix}@{domain}"