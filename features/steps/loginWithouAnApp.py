from behave import *
import time
import logging

from selenium.webdriver import Keys

from factory.webdriver_factory import get_driver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

URL = "https://inbound-induction-frontend-test.vercel.app/"


class TestE2E:

    @then('Select the "{station}"')
    def step_impl(context, station):
        btn_user = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 "//button[@class='MuiButtonBase-root MuiIconButton-root MuiIconButton-colorPrimary MuiIconButton-sizeMedium css-1ef184h']"))
        )
        btn_user.click()

        btn_change_station = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 "//li[normalize-space()='Cambiar estación']"))
        )
        btn_change_station.click()

        input_station = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable(
                (By.CSS_SELECTOR,
                 "body > div:nth-child(6) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > form:nth-child(2) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > div:nth-child(2) > input:nth-child(1)")))
        time.sleep(1)
        input_station.send_keys(station)

        first_option = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 '//*[@id=":r7:-listbox"]')))
        first_option.click()

        change_station = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 "//button[normalize-space()='Cambiar estación']")))
        change_station.click()


@then('Veloz without an app "{email_user}" "{type_Of_User}"')
def step_impl(context, email_user, type_Of_User):
    btn_veloz_no_app = WebDriverWait(context.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH,
                 "//button[normalize-space()='Veloz sin app móvil']")))
    btn_veloz_no_app.click()
    time.sleep(1)

    # input_user = WebDriverWait(context.driver, 25).until(
    #     EC.element_to_be_clickable(
    #         (By.XPATH,
    #         '//*[@id="form-no-app"]/div[1]/div[1]/div/div')))
    # input_user.click()
    # time.sleep(5)
    # input_user.send_keys("Lendaly")

    type_user = WebDriverWait(context.driver, 10).until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR,
             "#ProviderType")))
    type_user.send_keys(type_Of_User)
