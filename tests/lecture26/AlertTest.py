import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoAlertPresentException


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    #     # driver.maximize_window()
    yield driver
    driver.quit()

    wait = WebDriverWait(driver, 10)


def get_wait10(driver):
    return WebDriverWait(driver, 10)


def go_to_alerts(driver):
    driver.get("https://www.selenium.dev/selenium/web/alerts.html")


def test_read_alert(driver):
    go_to_alerts(driver)
    driver.find_element(By.ID, "alert").click()
    alert = driver.switch_to.alert
    alert_text = alert.text
    assert alert_text == "cheese"
    time.sleep(3)


def test_slow_alert(driver):
    go_to_alerts(driver)
    driver.find_element(By.ID, "slow-alert").click()

    get_wait10(driver).until(EC.alert_is_present())
    alert_text = driver.switch_to.alert.text
    assert alert_text == "Slow"
    time.sleep(3)


def test_slow_alert2(driver):
    go_to_alerts(driver)
    driver.find_element(By.ID, "slow-alert").click()
    alert = get_wait10(driver).until(EC.alert_is_present())
    assert alert.text == "Slow"


def test_click_ok_on_alert(driver):
    go_to_alerts(driver)
    driver.find_element(By.ID, "alert").click()
    time.sleep(2)
    driver.switch_to.alert.accept()

    try:
        driver.switch_to.alert

        assert False, (
            "Expected NoAlertPresentException "
            "to be thrown, but it wasn't"
        )

    except NoAlertPresentException:
        pass

    time.sleep(3)


def test_click_ok_on_alert2(driver):
    go_to_alerts(driver)
    driver.find_element(By.ID, "alert").click()
    time.sleep(2)
    alert = driver.switch_to.alert
    alert.accept()

    with pytest.raises(NoAlertPresentException):
        driver.switch_to.alert.text

    time.sleep(3)


def test_accept_alert(driver):
    go_to_alerts(driver)

    driver.find_element(By.ID, "confirm").click()
    time.sleep(3)
    alert = driver.switch_to.alert
    alert.accept()
    heading = driver.find_element(By.TAG_NAME, "h1").text
    assert heading == "Heading"
    time.sleep(3)


def test_dismiss_alert(driver):
    go_to_alerts(driver)
    driver.find_element(By.ID, "confirm").click()
    driver.switch_to.alert.dismiss()
    time.sleep(4)
    text = driver.find_element(By.TAG_NAME, "h1").text
    assert text == "Testing Alerts and Stuff"
    time.sleep(3)


def test_accept_prompt(driver):
    go_to_alerts(driver)

    driver.find_element(By.ID, "prompt").click()
    time.sleep(3)

    alert = get_wait10(driver).until(EC.alert_is_present())
    entered_text = "XXXXXSomedtfsgdsgsdfgsdfgsdfgsdfgsdfgsdqrsning something---"
    alert.send_keys(entered_text)
    # NOT DISPLAYING
    time.sleep(2)
    alert.accept()

    js = driver.execute_script
    js("window.scrollTo(0, document.body.scrollHeight)")
    # driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    # scroll up
    # driver.execute_script("window.scrollTo(0, 0)")

    actual_text = driver.find_element(By.XPATH, "//div[@id='text']/p").text
    assert actual_text == entered_text
    time.sleep(3)

