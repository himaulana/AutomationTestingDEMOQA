from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class ConfigDriver:
    BY = By
    WAIT = WebDriverWait
    EC = expected_conditions

    @classmethod
    def setup_class(cls):
        base_url = 'https://demoqa.com/automation-practice-form'
        options = cls.options()
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.get(base_url)
        cls.driver.implicitly_wait(5)

    def options():
        options = webdriver.ChromeOptions()
        options.page_load_strategy = 'eager'
        options.add_experimental_option('detach', True)

        return options
