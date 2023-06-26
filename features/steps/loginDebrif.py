from behave import *
import time
import logging
from factory.webdriver_factory import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


URL = "https://inbound-induction-frontend-test.vercel.app/"


class TestDebrif:

    @given('Launch Browser')
    def step_impl(context):
        context.driver = get_driver()
        context.driver.maximize_window()
        context.driver.implicitly_wait(10)

    @when('Open Debrif Dev')
    def step_impl(context):
        context.driver.get(URL)

    @then('login with user credential "{email}" "{pwd}"')
    def step_impl(context, email, pwd):
        input_email = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "loginfmt"))
        )
        input_email.send_keys(email)
        time.sleep(1)

        btn_next = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "idSIButton9"))
        )
        btn_next.click()
        time.sleep(1)

        input_pwd = WebDriverWait(context.driver, 10).until(
            EC.presence_of_element_located((By.NAME, "passwd"))
        )
        input_pwd.send_keys(pwd)
        time.sleep(1)

        btn_login = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "idSIButton9"))
        )
        btn_login.click()

        time.sleep(1)

        btn_accept = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable((By.ID, "idSIButton9"))
        )
        btn_accept.click()
        time.sleep(1)

    @then('Close Debrif')
    def step_impl(context):
        context.driver.quit()


