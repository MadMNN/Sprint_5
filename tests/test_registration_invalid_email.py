from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_registration_with_invalid_email(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    # Шаг 1: Вход и регистрация
    driver.find_element(By.XPATH, "//button[contains(text(), 'Вход и регистрация')]").click()

    # Шаг 2: Нет аккаунта
    WebDriverWait(driver, 5).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(text(), 'Нет аккаунта')]"))
    ).click()

    # Шаг 3: Ввод невалидного email
    driver.find_element(By.NAME, "email").send_keys("цваи")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Создать аккаунт')]").click()

    # Шаг 4: Проверка текста «Ошибка» под email
    error_span = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.XPATH, "//span[contains(@class, 'input_span') and text()='Ошибка']"))
    )
    assert error_span.is_displayed(), "Не отображается сообщение 'Ошибка' под полем email"

    # Шаг 5: Проверка красной рамки у поля email (по классу или стилю)
    email_field = driver.find_element(By.NAME, "email")
    class_attr = email_field.get_attribute("class")
    assert "error" in class_attr or "invalid" in class_attr or "input" in class_attr, \
        f"Поле email не содержит признаков ошибки: class='{class_attr}'"

    # готов
