import time
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.remote.webdriver import WebDriver

from tests.jenkins.NewItemPage import NewItemPage


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


title_item_in_table = (By.XPATH, "//a/span[contains(text(), 'Test Folder')]")
button_rename = (By.XPATH, "//a[contains(@href, 'confirm-rename')]")
input_new_name = (By.XPATH, "//input[@name='newName']")
button_submit = (By.XPATH, "//button[@name='Submit']")


@pytest.mark.dependency(name="create_test_folder")
def test_crete_folder(browser):
    ex_name_folder = "Test Folder"
    element_is_clickable(driver = browser, locator = button_new_item_locator).click()
    element_is_visible(browser, input_name_locator).send_keys(ex_name_folder)
    element_is_clickable(browser, list_folder_locator).click()
    element_is_clickable(browser, button_submit_locator).click()
    element_is_visible(browser, input_description).send_keys("Test Description")
    element_is_clickable(browser, button_save).click()
    browser.get("http://localhost:8080/")
    ac_name_folder = element_is_visible(browser, locator = table_name_folder).text
    assert (
            ac_name_folder == ex_name_folder
    ), f"Expected: {ex_name_folder} Actual: {ac_name_folder}"


@pytest.mark.dpendency(depends=["create_test_folder"])
def test_rename_folder(browser):
    old_name = "Test Folder"
    new_name = "New Folder"
    browser.get("http://localhost:8080/")
    time.sleep(2)
    element_is_clickable(browser, title_item_in_table).click()
    time.sleep(1)
    element_is_visible(browser, button_rename).click()
    element_is_visible(browser, input_new_name).clear()
    element_is_visible(browser, input_new_name).send_keys(new_name)
    element_is_visible(browser, button_submit).click()
    time.sleep(3)
    new_item_p = NewItemPage(driver=browser)
