import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

input_name_locator = (By.ID, "firstName")


def test_form():
    print("Attempting to open Chrome...")

    # driver = webdriver.Chrome()

    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    service = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)

    try:
        # Открытие страницы
        print("Открытие тестовой страницы (https://demoqa.com/automation-practice-form)...")
        driver.get("https://demoqa.com/automation-practice-form")

        driver.find_element(*input_name_locator).send_keys("Anna")

        time.sleep(3)

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        print("Закрытие браузера...")
        driver.quit()


if __name__ == "__main__":
    main()

# if __name__ == "__main__":
#     test_form()

