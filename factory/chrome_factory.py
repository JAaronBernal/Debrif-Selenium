from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from config.config_model import ConfigData


def create_driver(config: ConfigData):
    chrome_service = Service(config.get_drivers_path())

    return webdriver.Chrome(service=chrome_service)
