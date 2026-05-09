import time
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.remote.webdriver import WebDriver


def element_is_visible(driver: WebDriver, locator: tuple[str, str], timeout=30) -> WebElement:
    return wait(driver, timeout).until(EC.visibility_of_element_located(locator))


def elements_are_visible(driver: WebDriver, locator: tuple[str, str], timeout=30) -> list[WebElement]:
    return wait(driver, timeout).until(EC.visibility_of_all_elements_located(locator))


def element_is_present(driver: WebDriver, locator: tuple[str, str], timeout=30) -> WebElement:
    return wait(driver, timeout).until(EC.presence_of_element_located(locator))


def elements_are_present(driver: WebDriver, locator: tuple[str, str], timeout=30) -> list[WebElement]:
    return wait(driver, timeout).until(EC.presence_of_all_elements_located(locator))


def element_is_not_visible(driver: WebDriver, locator: tuple[str, str], timeout=30) -> WebElement:
    return wait(driver, timeout).until(EC.invisibility_of_element_located(locator))


def element_is_clickable(driver: WebDriver, locator: tuple[str, str], timeout=30) -> WebElement:
    return wait(driver, timeout).until(EC.element_to_be_clickable(locator))


button_new_item_locator = (By.XPATH, "//a[contains(., 'New Item')]")
input_name_locator = (By.XPATH, "//input[@id='name']")
list_folder_locator = (By.XPATH, "//li[span[contains(text(), 'Folder')]]")
button_submit_locator = (By.XPATH, "//button[@type='submit']")
input_description = (By.XPATH, "//textarea[@name='description']")
button_save = (By.XPATH, "//button[value='Save']")
description_folder = (By.XPATH, "//div[contains(text(), 'Test Description')]")
table_name_folder = (By.XPATH, "//tbody/tr/td[3]")
error_message = (By.XPATH, "//div[@id='itemname-invalid']")


def test_01(driver, login_admin):
    ex_name_folder = "Test Folder"
    element_is_clickable(driver, button_new_item_locator).click()
    element_is_visible(driver, input_name_locator).send_keys(ex_name_folder)
    element_is_clickable(driver, list_folder_locator).click()
    element_is_clickable(driver, button_submit_locator).click()
    element_is_visible(driver, input_description).send_keys("Test Description")
    element_is_clickable(driver, button_save).click()
    driver.get("http://localhost:8080/")
    ac_name_folder = element_is_visible(driver, table_name_folder).text
    assert (
            ac_name_folder == ex_name_folder
    ), f"Expected: {ex_name_folder} Actual: {ac_name_folder}"


def test_02(driver, login_admin):
    name_folder = "!"
    sys_message_default_str = "is an unsafe character"
    element_is_clickable(driver, button_new_item_locator).click()
    element_is_visible(driver, input_name_locator).send_keys(name_folder)

    ex_error_message = f"» ‘{name_folder}’ {sys_message_default_str}"
    ac_error_message = element_is_visible(driver, error_message).text
    assert ac_error_message == ex_error_message


def test_03(driver, folder):
    pass