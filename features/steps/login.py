from behave import *
import time
from factory.webdriver_factory import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

URL = "https://authsandbox.99minutos.com/"


class TestLaboratorioQAMinds:
    @given('Launch in Browser')
    def step_impl(context):
        context.driver = get_driver()
        context.driver.implicitly_wait(10)
        context.wait_driver = WebDriverWait(context.driver, 8)
        context.driver.maximize_window()

    @when('Open Selfservices Sandbox')
    def step_impl(context):
        context.driver.get(URL)

    @then('login with credential "{email}" "{pwd}"')
    def step_impl(context, email,pwd):
        userName = context.driver.find_element(By.CSS_SELECTOR, "form > :nth-child(1) > input")
        assert userName.is_displayed() and userName.is_enabled(), "El campo de busqueda tiene que estar visible y habilitado"
        userName.send_keys(email)
        time.sleep(1)

        password = context.driver.find_element(By.CSS_SELECTOR, ":nth-child(2) > input")
        assert password.is_displayed() and password.is_enabled(), "El campo de busqueda tiene que estar visible y habilitado"
        password.send_keys(pwd)
        time.sleep(1)

        btnLoggin =context.driver.find_element(By.CSS_SELECTOR,".Button_button__17TMH")
        assert btnLoggin.is_displayed() and btnLoggin.is_enabled(), "El campo de busqueda tiene que estar visible y habilitado"
        btnLoggin.click()
        time.sleep(1)

    @then('Close Selfservices')
    def step_impl(context):
        context.driver.quit()
