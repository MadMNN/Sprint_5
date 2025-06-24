import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_create_ad_authorized(driver):
    driver.maximize_window()
    driver.get("https://qa-desk.stand.praktikum-services.ru/")
    wait = WebDriverWait(driver, 10)

    # Авторизация
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Вход и регистрация')]"))).click()
    wait.until(EC.visibility_of_element_located((By.NAME, "email"))).send_keys("m.l.mihailov@yandex.ru")
    driver.find_element(By.NAME, "password").send_keys("12345678")
    driver.find_element(By.XPATH, "//button[contains(text(), 'Войти')]").click()

    # Ждём, пока модалка исчезнет (если появилась)
    try:
        WebDriverWait(driver, 5).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "homePage_modal__zSdUB"))
        )
    except:
        pass

    # Переход к созданию объявления
    wait.until(EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Разместить объявление')]"))).click()

    # Ввод названия
    wait.until(EC.visibility_of_element_located((By.NAME, "name"))).send_keys("Автотест: Книга")

    # Универсальная функция для выбора значения из выпадающего списка
    def select_dropdown_option(option_text):
        xpath = f"//button[@type='button']//span[text()='{option_text}']"
        option = wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
        driver.execute_script("arguments[0].scrollIntoView(true);", option)
        option.click()

    # Выбор категории
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='category']/following-sibling::button"))).click()
    select_dropdown_option("Книги")

    # Выбор города
    wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@name='city']/following-sibling::button"))).click()
    select_dropdown_option("Нижний Новгород")

    # Выбор состояния товара "Б/У"
    condition_radio = driver.find_element(By.XPATH, "//input[@name='condition' and @value='Б/У']")
    driver.execute_script("arguments[0].click();", condition_radio)

    # Ввод описания по placeholder
    wait.until(EC.visibility_of_element_located((By.XPATH, "//textarea[@placeholder='Описание товара']"))).send_keys("Тестовое описание товара")

    # Ввод стоимости по placeholder
    wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Стоимость']"))).send_keys("1234")

    WebDriverWait(driver, 5).until(lambda d: True)

    # Публикация объявления
    driver.find_element(By.XPATH, "//button[contains(text(), 'Опубликовать')]").click()



    # Переход в "Мои объявления"

 
    WebDriverWait(driver, 15).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.circleSmall"))
    ).click()



    # Проверка, что объявление отобразилось
    ad_title = wait.until(EC.visibility_of_element_located((By.XPATH, "//h2[@class='h2' and text()='Автотест: Книга']")))
    assert ad_title is not None