import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

@pytest.mark.dependency(name="login")
def test_login():
    driver.get("https://example.com/login")
    driver.find_element(By.ID, "email").send_keys("test@mail.com")
    driver.find_element(By.ID, "password").send_keys("123456")
    driver.find_element(By.ID, "loginBtn").click()

    assert driver.find_element(By.ID, "profile").is_displayed()


@pytest.mark.dependency(depends=["login"])
def test_profile():
    driver.find_element(By.ID, "profile").click()
    assert "profile" in driver.current_url


@pytest.mark.dependency(depends=["login"])
def test_logout():
    driver.find_element(By.ID, "logout").click()
    assert "login" in driver.current_url

    # pytest-dependency



    # | Подход                | Java (TestNG)    | Python (pytest)   |
    # | --------------------- | ---------------- | ----------------- |
    # | Зависимости           | dependsOnMethods | pytest-dependency |
    # | Лучший подход         | ❌ зависимость   | ✅ fixtures       |
    # | Управление состоянием | через driver     | через fixtures    |