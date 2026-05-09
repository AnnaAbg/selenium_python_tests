import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    #     # driver.maximize_window()
    yield driver
    driver.quit()


def go_to_iframes(driver):
    driver.get("https://www.selenium.dev/selenium/web/iframes.html")


def go_to_other_iframes(driver):
    driver.get("https://www.selenium.dev/selenium/web/slow_loading_iframes.html")


def test_element_in_iframes(driver):
    go_to_iframes(driver)

    try:
        print(driver.find_element(By.ID, "email"))
        assert False  # there shouldn't be one

    except NoSuchElementException:
        print("Element can't be found, and that's correct!")

    frame = driver.find_element(By.ID, "iframe1")
    driver.switch_to.frame(frame)
    email = driver.find_element(By.ID, "email")
    assert email.tag_name == "input"

def test_element_outside_iframe(driver):
    go_to_iframes(driver)
    assert driver.find_element(By.ID, "iframe_page_heading").tag_name == "h1"
    driver.switch_to.frame("iframe1")

    try:
        driver.find_element(By.ID, "iframe_page_heading")
        assert False, "Expected the element iframe_page_heading to be missing"  # shouldn't be accessible
    except NoSuchElementException:
        print("Element can't be found, and that's correct!")

    driver.switch_to.default_content()
    assert driver.find_element(By.ID, "iframe_page_heading").tag_name == "h1"


def test_switch_between_iframes(driver):
    go_to_other_iframes(driver)
    second_frame = driver.find_element(By.ID, "noSrc")
    # driver.switch_to.frame("noSrc")
    driver.switch_to.frame(second_frame)
    driver.switch_to.default_content()
    driver.switch_to.frame(0)
    assert driver.find_element(By.ID, "announcement-banner").tag_name == "section"
