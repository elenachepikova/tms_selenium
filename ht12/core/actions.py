import allure
from selenium.webdriver.firefox.webdriver import WebDriver


class Actions:
    def __init__(self, driver):
        self.driver: WebDriver = driver

    @allure.step('Find element by selector')
    def get_element(self, selector):
        return self.driver.find_element(*selector)

    @allure.step('Click_on ${selector}')
    def click_on(self, selector, force=False):
        element = self.get_element(selector)
        if force:
            self.driver.execute_script("arguments[0].click();", element)
        else:
            element.click()

    @allure.step('Fill in the field with {text}')
    def send_text(self, text, selector):
        field = self.get_element(selector)
        field.send_keys(text)
        assert field.get_attribute("value") == text

    @allure.step('Clear text field')
    def clear_text(self, selector):
        field = self.get_element(selector)
        field.clear()
        assert field.get_attribute("value") == ''
