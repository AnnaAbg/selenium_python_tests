from selenium import webdriver
from selenium.webdriver.common.by import By


def test_color_picker():
    driver = webdriver.Chrome()
    try:
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")

        driver.implicitly_wait(0.5)

        color_picker = driver.find_element(by=By.NAME, value="my-colors")

        current_color = color_picker.get_attribute("value")
        print(f"Текущий цвет: {current_color}")

        assert current_color == "#563d7c", f"Ожидался #563d7c, получен {current_color}"

        print("✓ Цвет установлен корректно!")

    finally:
        driver.quit()


def test_data_picker():
    driver = webdriver.Chrome()

    try:
        driver.get("https://www.selenium.dev/selenium/web/web-form.html")

        driver.implicitly_wait(0.5)

        data_picker = driver.find_element(By.NAME, "my-date")

        data_picker.click()
        data_picker.clear()
        data_picker.send_keys("04/10/2026")

        # current_date = data_picker.get_attribute("value")

        # print(f"Current date: {current_date}")

        # assert current_date == "04/10/2026"
        assert data_picker.get_attribute("value") == "04/10/2026"

        # print("✓ Date is set up correctly!")

    finally:
        driver.quit()




# ⚖️ Key difference
# Type	Example	Meaning
# in	A in B	partial match ✔
# ==	A == B	exact match ✔
# 🧠 Simple mental model
# 🔎 in = “is it somewhere inside?”
# URL contains word?
# 🎯 == = “is it exactly the same?”
# Value must match 100%
# 🚀 Real QA examples
# ✔ URL check (flexible)
# assert "login" in current_url
# ✔ form validation (strict)
# assert username == "admin"


