from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_guest_cannot_post_ad(driver):
    driver.get("https://qa-desk.stand.praktikum-services.ru/")

    # Шаг 1: Кликаем по кнопке «Разместить объявление»
    driver.find_element(By.XPATH, "//button[contains(text(), 'Разместить объявление')]").click()

    # Шаг 2: Проверяем, что появилось модальное окно с нужным заголовком
    modal_header = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((
            By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]"
        ))
    )


    assert modal_header.is_displayed(), "Модальное окно с заголовком не появилось"

    # готов