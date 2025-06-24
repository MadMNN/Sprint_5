
from selenium.webdriver.common.by import By

# Авторизация
LOGIN_BUTTON = (By.XPATH, "//button[contains(., 'Вход и регистрация')]")
EMAIL_INPUT = (By.NAME, "email")
PASSWORD_INPUT = (By.NAME, "password")
SUBMIT_LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")

# Создание объявления
CREATE_AD_BUTTON = (By.XPATH, "//button[contains(., 'Разместить объявление')]")
TITLE_INPUT = (By.NAME, "name")
CATEGORY_DROPDOWN = (By.XPATH, "//input[@name='category']/following-sibling::button")
CITY_DROPDOWN = (By.XPATH, "//input[@name='city']/following-sibling::button")
CONDITION_USED_RADIO = (By.XPATH, "//input[@name='condition' and @value='Б/У']")
DESCRIPTION_TEXTAREA = (By.XPATH, "//textarea[@placeholder='Описание товара']")
PRICE_INPUT = (By.XPATH, "//input[@placeholder='Стоимость']")
PUBLISH_BUTTON = (By.XPATH, "//button[contains(text(), 'Опубликовать')]")

# Навигация и проверка
MY_ADS_BUTTON = (By.XPATH, "//a[contains(@href, '/my-items')]")  # более специфичный путь
def AD_TITLE(title): return (By.XPATH, f"//h2[@class='h2' and text()='{title}']")
def AD_CITY(city): return (By.XPATH, f"//h3[@class='h3' and text()='{city}']")

# Универсальный локатор для выпадающих значений
def DROPDOWN_OPTION(option_text):
    return (By.XPATH, f"//button[@type='button']//span[text()='{option_text}']")
