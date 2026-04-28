from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def test_form2():
    # 1. Define your options
    options = Options()
    # This prevents the "Chrome is being controlled by automated software" bar
    options.add_experimental_option('excludeSwitches', ['enable-automation'])
    # This bypasses additional bot-detection hangs
    options.add_argument("--disable-blink-features=AutomationControlled")

    # 2. Start the driver WITHOUT using ChromeDriverManager
    # Selenium 4 handles the Service and Manager internally now
    driver = webdriver.Chrome(options=options)

    try:
        print("Browser started successfully!")
        driver.get("https://demoqa.com/automation-practice-form")

        # Add a small print to confirm the page loaded in the 'Run' window
        print(f"Current Title: {driver.title}")

    finally:
        # Close the browser
        driver.quit()
