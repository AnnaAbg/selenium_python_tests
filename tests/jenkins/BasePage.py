from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.home_url = "http://localhost:8080/"

    def go_home_page(self):
        self.driver.get(self.home_url)

    def element_is_visible(self, locator, timeout=30) -> WebElement:
        return wait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def elements_visible(self, locator, timeout=30) -> list[WebElement]:
        return wait(self.driver, timeout).until(
            EC.visibility_of_all_elements_located(locator)
        )

    def element_is_present(self, locator, timeout=30) -> WebElement:
        return wait(self.driver, timeout).until(
            EC.presence_of_element_located(locator)
        )

    def elements_are_present(self, locator, timeout=30) -> list[WebElement]:
        return wait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def element_is_not_visible(self, locator, timeout=30):
        return wait(self.driver, timeout).until(
            EC.invisibility_of_element_located(locator)
        )

    def element_is_clickable(self, locator, timeout=30):
        return wait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )