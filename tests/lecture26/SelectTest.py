import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


#  driver = webdriver.Chrome()
# dropdown = Select(driver.find_element(By.ID, "dropdown_id"))

# dropdown.select_by_visible_text("Option 1")
# Other options:
# dropdown.select_by_value("value1")
# dropdown.select_by_index(1)

def go_to_web_form(driver):
    # driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/web/selectPage.html")


def test_simple_dropdown():
    # WebDriver driver = new ChromeDriver();
    driver = webdriver.Chrome()
    # driver.get("selectPage.html");
    # driver.get("https://www.selenium.dev/selenium/web/selectPage.html");
    driver.get("https://www.selenium.dev/selenium/web/selectPage.html")
    # final WebElement  selectWithoutMultiple = driver.findElement(By.id("selectWithoutMultiple"));
    select_without_multiple = driver.find_element(By.ID, "selectWithoutMultiple")
    # Select simpleDropDown = new Select(selectWithoutMultiple);
    simple_dropdown = Select(select_without_multiple)
    time.sleep(2)

    # simpleDropDown.selectByValue("two");
    simple_dropdown.select_by_value("two")

    # String newValue = selectWithoutMultiple.getAttribute("value");
    new_value = select_without_multiple.get_attribute("value")
    # System.out.println(newValue);
    print(new_value)

    # Assert.assertEquals(newValue, "two");
    assert new_value == "two"
    time.sleep(2)
    driver.quit()


def test_multiple_select():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/web/selectPage.html")
    select_element = driver.find_element(By.ID, "selectWithMultipleEqualsMultiple")

    multi_select = Select(select_element)

    multi_select.select_by_index(1)
    multi_select.select_by_index(2)
    time.sleep(2)

    multi_select.deselect_by_index(0)
    time.sleep(2)

    multi_select.select_by_visible_text("Cheddar")

    print(select_element.get_attribute("value"))

    #     System.out.println(
    #             multiSelect.getAllSelectedOptions().stream()
    #                     .map(WebElement::getText).collect(Collectors.toList()));

    selected_texts = [option.text for option in multi_select.all_selected_options]
    print(f"Selected Options: {selected_texts}")

    time.sleep(3)
    driver.quit()


def test_long_list():
    driver = webdriver.Chrome()
    # driver.get("https://www.selenium.dev/selenium/web/selectPage.html")
    go_to_web_form(driver)
    select_element = driver.find_element(By.ID, "selectWithMultipleLongList")
    my_favorite_select = Select(select_element)
    my_favorite_select.select_by_visible_text("five")
    my_favorite_select.select_by_visible_text("six")

    print(select_element.get_attribute("value"))

    #     System.out.println(myFavoriteSelect.getAllSelectedOptions()
    #             .stream()
    #             .map(webElement -> webElement.getText())
    #             .collect(Collectors.toList()));

    print([opt.text for opt in my_favorite_select.all_selected_options])
    # 5. Get all selected options using List Comprehension (The Stream/Map equivalent)
    # selected_texts = [opt.text for opt in my_favorite_select.all_selected_options]
    # print(selected_texts)

    time.sleep(3)
    driver.quit()

# Feature,Java Code (Your Snippet),                                    Python Code (Above)
# Method Name,public void testMultipleSelect(),                        def test_multiple_select():
# Sleep,Thread.sleep(2000);,                                           "time.sleep(2) (Seconds, not MS)"
# Select Methods,selectByIndex(1),                                     select_by_index(1)
# Get Attribute,"getAttribute(""value"")",                             "get_attribute(""value"")"
# List Processing,.stream().map(WebElement::getText).collect(...),     [opt.text for opt in multi_select.all_selected_options]
# Exceptions,throws Exception,                                          Not required for time.sleep


# The "List Comprehension" Superpower
# In your Java code, you used a Stream to get the text of all selected options:
# multiSelect.getAllSelectedOptions().stream().map(WebElement::getText).collect(Collectors.toList())
#
# In Python, the List Comprehension is the preferred way to do this:
# [option.text for option in multi_select.all_selected_options]
#
# It is significantly shorter and achieves exactly the same result (a list of strings).


# Understanding the Stream vs. List Comprehension
# Your Java code uses a functional pipeline to extract text from a list of elements:
# myFavoriteSelect.getAllSelectedOptions().stream().map(el -> el.getText()).collect(...)
#
# In Python, the logic is "inside out" and much more concise:
# [opt.text for opt in my_favorite_select.all_selected_options]
#
# opt.text: This is your Map step (getting the text attribute).
#
# for opt in ...: This is your Stream step (iterating over the list).
#
# [...]: These brackets are your Collect step (putting the results back into a list).
