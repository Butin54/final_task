#  python -m pytest -v -s --driver Chrome --driver-path D:/chromedriver.exe tests/test_start_veb.py


import settings
from pages.rt import MainPage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_auth_code1(web_browser):
    """ Авторизация по коду корректный email. """

    page = MainPage(web_browser)

    WebDriverWait(web_browser, 125).until(EC.invisibility_of_element((By.CSS_SELECTOR, "div.otp-form__timeout")))
    page.email_or_phone = settings.email_or_phone_var[0]
    page.get_code.click()

    assert page.search_title.get_text() == 'Код подтверждения отправлен'

def test_auth_code2(web_browser):
    """ Авторизация по коду в формате email. """

    page = MainPage(web_browser)

    WebDriverWait(web_browser, 125).until(EC.invisibility_of_element((By.CSS_SELECTOR, "div.otp-form__timeout")))
    page.email_or_phone = settings.email_or_phone_var[1]
    page.get_code.click()

    assert page.search_title.get_text() == 'Код подтверждения отправлен'

def test_auth_code3(web_browser):
    """ Авторизация по коду спецсимволы. """

    page = MainPage(web_browser)

    page.email_or_phone = settings.email_or_phone_var[2]
    page.get_code.click()
    WebDriverWait(web_browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                        "span.rt-input-container__meta.rt-input-container__meta--error")))

    assert page.container_error.get_text() != ''

def test_auth_code4(web_browser):
    """ Авторизация по коду кириллица. """

    page = MainPage(web_browser)

    page.email_or_phone = settings.email_or_phone_var[3]
    page.get_code.click()
    WebDriverWait(web_browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                        "span.rt-input-container__meta.rt-input-container__meta--error")))

    assert page.container_error.get_text() != ''

def test_auth_code5(web_browser):
    """ Авторизация по коду длинная строка. """

    page = MainPage(web_browser)

    page.email_or_phone = settings.email_or_phone_var[4]
    page.get_code.click()
    WebDriverWait(web_browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                        "span.rt-input-container__meta.rt-input-container__meta--error")))

    assert page.container_error.get_text() != ''

def test_auth_code6(web_browser):
    """ Авторизация по коду пустая строка. """

    page = MainPage(web_browser)

    page.email_or_phone = settings.email_or_phone_var[5]
    page.get_code.click()
    WebDriverWait(web_browser, 5).until(EC.visibility_of_element_located((By.CSS_SELECTOR,
                        "span.rt-input-container__meta.rt-input-container__meta--error")))

    assert page.container_error.get_text() != ''

def test_auth_code7(web_browser):
    """ Авторизация по коду телефон в формате +7**********. """

    page = MainPage(web_browser)

    WebDriverWait(web_browser, 125).until(EC.invisibility_of_element((By.CSS_SELECTOR, "div.otp-form__timeout")))
    page.email_or_phone = settings.email_or_phone_var[6]
    page.get_code.click()

    assert page.search_title.get_text() == 'Код подтверждения отправлен'

def test_auth_code8(web_browser):
    """ Авторизация по коду телефон в формате 8**********. """

    page = MainPage(web_browser)

    WebDriverWait(web_browser, 125).until(EC.invisibility_of_element((By.CSS_SELECTOR, "div.otp-form__timeout")))
    page.email_or_phone = settings.email_or_phone_var[7]
    page.get_code.click()

    assert page.search_title.get_text() == 'Код подтверждения отправлен'

def test_auth_code9(web_browser):
    """ Авторизация по коду телефон в формате 9*********. """

    page = MainPage(web_browser)

    WebDriverWait(web_browser, 125).until(EC.invisibility_of_element((By.CSS_SELECTOR, "div.otp-form__timeout")))
    page.email_or_phone = settings.email_or_phone_var[8]
    page.get_code.click()

    assert page.search_title.get_text() == 'Код подтверждения отправлен'

def test_auth_code10(web_browser):
    """ Авторизация по коду строка из цифр > 11. """

    page = MainPage(web_browser)

    WebDriverWait(web_browser, 125).until(EC.invisibility_of_element((By.CSS_SELECTOR, "div.otp-form__timeout")))
    page.email_or_phone = settings.email_or_phone_var[9]
    page.get_code.click()

    assert page.container_error.get_text() != ''

def test_auth_pass1(web_browser):
    """ Авторизация с паролем по номеру телефона. """

    page = MainPage(web_browser)

    page.enter_with_pass.click()
    page.user_name = settings.email_or_phone_var[0]
    page.password = settings.valid_password
    page.enter_btn.click()

    assert page.get_current_url() == 'https://start.rt.ru/'

def test_auth_pass2(web_browser):
    """ Авторизация с паролем по почте. """

    page = MainPage(web_browser)

    page.enter_with_pass.click()
    page.tab_mail.click()
    page.user_name = settings.email_or_phone_var[0]
    page.password = settings.valid_password
    page.enter_btn.click()

    assert page.get_current_url() == 'https://start.rt.ru/'

def test_registration1(web_browser):
    """ Регистрация, заполнение поля имя латиницей. """

    page = MainPage(web_browser)

    page.enter_with_pass.click()
    page.registration.click()
    page.first_name = settings.name_var[0]
    page.register_btn.click()

    assert page.container_error.get_text() != ''

def test_registration2(web_browser):
    """ Регистрация, заполнение поля имя кириллицей. """

    page = MainPage(web_browser)

    page.enter_with_pass.click()
    page.registration.click()
    page.first_name = settings.name_var[2]
    page.register_btn.click()

    assert not page.container_error_name.is_presented()

def test_registration3(web_browser):
    """ Регистрация, заполнение поля фамилия латиницей. """

    page = MainPage(web_browser)

    page.enter_with_pass.click()
    page.registration.click()
    page.first_name = settings.name_var[2]
    page.last_name = settings.name_var[0]
    page.register_btn.click()

    assert page.container_error.get_text() != ''

def test_registration4(web_browser):
    """ Регистрация, заполнение поля фамилия кириллицей. """

    page = MainPage(web_browser)

    page.enter_with_pass.click()
    page.registration.click()
    page.first_name = settings.name_var[2]
    page.last_name = 'Иванов'
    page.register_btn.click()

    assert not page.container_error_lastname.is_presented()

