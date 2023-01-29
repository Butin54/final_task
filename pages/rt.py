import os

from pages.base import WebPage
from pages.elements import WebElement


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://start.rt.ru/'

        super().__init__(web_driver, url)

    # Поле для заполнения почты или пароля при авторизации по коду
    email_or_phone = WebElement(id='address')

    # Кнопка получить код
    get_code = WebElement(id='otp_get_code')

    # Заголовок страницы для введения временного кода
    search_title = WebElement(xpath='//h1')

    # Сообщение о ошибке при вводе
    container_error = WebElement(css_selector='span.rt-input-container__meta.rt-input-container__meta--error')

    # Кнопка войти с паролем
    enter_with_pass = WebElement(id='standard_auth_btn')

    # Поле для ввода телефона/почты/логина/лицевого счета
    user_name = WebElement(id='username')

    # Поле для ввода пароля
    password = WebElement(id='password')

    # Кнопка Войти
    enter_btn = WebElement(id='kc-login')

    # Таб переключения способа авторизации Почта
    tab_mail = WebElement(id='t-btn-tab-mail')

    # Ссылка Зарегистрироваться
    registration = WebElement(id='kc-register')

    # Поле ввода Имя
    first_name = WebElement(name='firstName')

    # Кнопка Зарегистрироваться
    register_btn = WebElement(name='register')

    # Сообщение об ошибке под полем Имя
    container_error_name = WebElement(xpath='//div.name-container/div[1]/span')

    # Поле ввода Фамилия
    last_name = WebElement(name='lastName')

    # Сообщение об ошибке под полем Фамилия
    container_error_lastname = WebElement(xpath='//div.name-container/div[2]/span')
