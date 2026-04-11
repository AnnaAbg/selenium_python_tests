import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()        #  WebDriver driver = new ChromeDriver();

driver.get("https://www.selenium.dev/selenium/web/web-form.html") # the same in Java

# title = driver.title                # driver.getTitle();

driver.implicitly_wait(0.5)         # driver.manage().timeouts().implicitlyWait(Duration.ofMillis(500));

text_box = driver.find_element(By.NAME, "my-text") #  WebElement textBox = driver.findElement(By.name("my-text"));
submit_button = driver.find_element(By.CSS_SELECTOR, "button") #  WebElement submitButton = driver.findElement(By.cssSelector("button"));
time.sleep(2)

text_box.send_keys("Selenium")       #  textBox.sendKeys("Selenium");
time.sleep(2)                        # Thread.sleep(2000);
submit_button.click()                #  submitButton.click();

message = driver.find_element(By.ID, "message")  #  WebElement message = driver.findElement(By.id("message"));
text = message.text                  #  message.getText();
# print(text)

# assert message.text == "Received!"
assert text == "Received!"
time.sleep(4)
driver.quit()  # the same in Java
