from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.helpers.auth import generate_unique_email
from tests.helpers.urls import *

def test_user_registration(driver):
    driver.get(MAIN_PAGE_URL)

    # Вход и регистрация
    driver.find_element(By.XPATH, "//button[contains(text(), 'Вход и регистрация')]").click()

    # Нет аккаунта
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Нет аккаунта')]"))
    ).click()

    # Заполнение формы
    driver.find_element(By.NAME, "name").send_keys("User")
    driver.find_element(By.NAME, "email").send_keys(generate_unique_email())
    driver.find_element(By.NAME, "password").send_keys("12345678")
    driver.find_element(By.NAME, "submitPassword").send_keys("12345678")

    # Создать аккаунт
    driver.find_element(By.XPATH, "//button[contains(text(), 'Создать аккаунт')]").click()

    # Проверка появления кнопки «Разместить объявление»
    post_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Разместить объявление')]"))
    )
    assert post_button.is_displayed()

    # Проверка аватара и имени пользователя
    avatar = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "circleSmall"))
    )
    user_name = driver.find_element(By.CLASS_NAME, "profileText")

    assert avatar.is_displayed()
    assert user_name.text == "User."

# готов