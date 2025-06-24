from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_user_login(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    # Нажимаем "Вход и регистрация"
    login_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Вход и регистрация')]"))
    )
    login_button.click()

    # Вводим email
    email_input = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "email"))
    )
    email_input.send_keys("m.l.mihailov@yandex.ru")

    # Вводим пароль
    password_input = driver.find_element(By.NAME, "password")
    password_input.send_keys("12345678")

    # Нажимаем "Войти"
    submit_button = driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]")
    submit_button.click()

    # Проверка аватара и имени пользователя
    avatar = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "circleSmall"))
    )
    user_name = driver.find_element(By.CLASS_NAME, "profileText")

    assert avatar.is_displayed()
    assert user_name.text == "User."

    # готов