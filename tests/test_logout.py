from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.helpers.urls import *

def test_user_logout(driver):
    driver.get(MAIN_PAGE_URL)

    # Шаг 1: открыть форму входа
    driver.find_element(By.XPATH, "//button[contains(text(), 'Вход и регистрация')]").click()

    # Шаг 2: авторизация
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Введите Email']"))
    ).send_keys("m.l.mihailov@yandex.ru")

    driver.find_element(By.XPATH, "//input[@placeholder='Пароль']").send_keys("12345678")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()

    # Шаг 3: убедиться, что вошли (появилось имя User)
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//h3[contains(@class, 'profileText') and contains(text(), 'User')]"))
    )

    # Шаг 4: нажать кнопку "Выйти"
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Выйти')]"))
    ).click()

    # Шаг 5: ожидание возврата кнопки «Вход и регистрация»
    WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "//button[contains(text(), 'Вход и регистрация')]"))
    )

# Шаг 6: убедиться, что блок User исчез
    WebDriverWait(driver, 5).until(
        EC.invisibility_of_element_located((By.XPATH, "//h3[contains(@class, 'profileText') and contains(text(), 'User.')]"))
)

# Финальная проверка: убедиться, что кнопка входа снова отображается
    assert driver.find_element(By.XPATH, "//button[contains(text(), 'Вход и регистрация')]").is_displayed()