import time

import pytest
from selenium.webdriver.common.by import By
from tests.jenkins.BasePage import BasePage

button_new_item_locator = (By.XPATH, "//a[contains(., 'New Item')]")
input_name_locator = (By.XPATH, "//input[@id='name']")
list_folder_locator = (By.XPATH, "//li[span[contains(text(), 'Folder')]]")
button_submit_locator = (By.XPATH, "//button[@type='submit']")
input_description = (By.XPATH, "//textarea[@name='description']")
button_save = (By.XPATH, "//button[value='Save']")
description_folder = (By.XPATH, "//div[contains(text(), 'Test Description')]")
table_name_folder = (By.XPATH, "//tbody/tr/td[3]")
error_message = (By.XPATH, "//div[@id='itemname-invalid']")


class NewItemPage(BasePage):


 def __init__(self, driver):
    super().__init__(driver)


def click_new_item(self):
    self.lement_is_clickable(button_new_item_locator).click()


def input_name_new_folder(self, name):
    self.element_is_visible(input_name_locator).send_keys(name)


def set_folder_in_list_items(self):
    self.element_is_visible(list_folder_locator).click()


def test_create_folder(self, name):
    ex_name_folder = "Test Folder"
    self.click_new_item()
    self.input_name_new_folder(name=name)
    self.set_folder_in_list_items()
    self.element_is_clickable(button_submit_locator).click()
    self.element_is_visible(input_description).send_keys("Test Description")
    self.element_is_clickable(button_save).click()
    self.driver.get("http://localhost:8080/")
    time.sleep(2)
    ac_name_folder = self.element_is_visible(locator=table_name_folder).text
    assert (
            ac_name_folder == ex_name_folder
    ), f"Expected: {ex_name_folder}, Actual: {ac_name_folder}"


@pytest.mark.dependency(name="test_create_folder")
def test_create_folder_2(browser):
    new_item_p = NewItemPage(driver=browser)
    new_item_p.create_folder(name="Test Folder")