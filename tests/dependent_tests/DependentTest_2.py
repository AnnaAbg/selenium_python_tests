import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture(scope="class")
def logged_in(driver):
    driver.get("https://example.com/login")
    driver.find_element(By.ID, "email").send_keys("test@mail.com")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "loginBtn").click()
    return driver


class TestUI:

    def test_profile(self, logged_in):
        logged_in.find_element(By.ID, "profile").click()
        assert "profile" in logged_in.current_url

    def test_logout(self, logged_in):
        logged_in.find_element(By.ID, "logout").click()
        assert "login" in logged_in.current_url


        # fixture с состоянием