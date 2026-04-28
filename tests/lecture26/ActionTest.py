# Public (Default):
# def go_to_web_form(self): — Anyone can call this.
#
# Internal/Protected (Convention):
# def _go_to_web_form(self): — This signals: "Please don't call this outside of this class or its subclasses."
#
# Private (Name Mangling):
# def __go_to_web_form(self): — Using two underscores makes it harder (but not impossible) to access from outside the class.
import time

import pytest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    #     # driver.maximize_window()
    yield driver
    driver.quit()


# yield
# 5. yield driver
#
# 👉 Это самая важная строка
#
# Она делает 2 вещи:
#
# ✅ 1. Отдаёт driver в тест
# def test_something(driver):
#
# 👉 тест получает этот driver
#
# ✅ 2. Делит функцию на 2 части:
#
# До yield → setup (подготовка)
# После yield → teardown (очистка)

# pytest запускает тест:
#
# 1. вызывает fixture
# 2. создаёт driver
# 3. yield → отдаёт driver в тест
# 4. выполняется тест
# 5. возвращается в fixture
# 6. выполняется driver.quit()

# Advanced way
# @pytest.fixture
# def driver():
#     options = webdriver.ChromeOptions()
#     options.add_argument("--start-maximized")
#
#     driver = webdriver.Chrome(options=options)
#     yield driver
#     driver.quit()

def go_to_web_form(driver):
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")


def go_to_drag_and_drop(driver):
    driver.get("https://www.selenium.dev/selenium/web/dragAndDropTest.html")


# Когда ActionChains НЕ нужен
# send_keys() на элементе
# click()
# get_attribute()
# обычные действия с элементами
#
# ➡️ Твой случай — именно такой ✅
#
# 🔥 Когда ActionChains НУЖЕН
#
# Используй ActionChains, если есть сложные действия:
#
# hover (наведение мыши)
# drag & drop
# удержание клавиш (key_down)
# цепочки действий
#
# Пример:
# from selenium.webdriver.common.action_chains import ActionChains
#
# actions = ActionChains(driver)
# actions.click_and_hold(source).move_to_element(target).release().perform()


def test_slider_arrow_keys(driver):
    # driver = webdriver.Chrome()
    go_to_web_form(driver)
    slider = driver.find_element(By.NAME, "my-range")
    time.sleep(2)
    slider.send_keys(Keys.LEFT, Keys.LEFT)
    time.sleep(2)
    slider.send_keys(Keys.LEFT, Keys.LEFT)
    assert slider.get_attribute("value") == "1"
    time.sleep(3)


def test_slider_arrow_keys2(driver):
    # driver = webdriver.Chrome()
    go_to_web_form(driver)
    slider1 = driver.find_element(By.NAME, "my-range")
    time.sleep(2)
    slider1.send_keys(Keys.LEFT)
    time.sleep(1)
    slider1.send_keys(Keys.LEFT, Keys.LEFT)
    assert slider1.get_attribute("value") == "2"
    time.sleep(3)


def test_slider_action(driver):
    go_to_web_form(driver)

    slider = driver.find_element(By.XPATH, "//input[@name='my-range']")
    time.sleep(1)

    ActionChains(driver) \
        .click_and_hold(slider) \
        .move_by_offset(-100, 0) \
        .release() \
        .perform()
    #         getActions() //Actions
    #                 .clickAndHold(slider) //Actions
    #                 .moveByOffset(-100, 0) //Actions
    #                 .release() //Actions
    #                 .perform(); //void
    #

    print(slider.get_attribute("value"))
    assert slider.get_attribute("value") == "1"
    time.sleep(3)


def test_slider_click(driver):
    go_to_web_form(driver)
    slider = driver.find_element(By.NAME, "my-range")
    size = slider.size
    slider_width = size["width"]

    #       final Dimension size = slider.getSize();
    #         int sliderWidth = size.getWidth();
    #
    time.sleep(1)

    ActionChains(driver) \
        .move_to_element(slider) \
        .move_by_offset(slider_width * 2 / 10, 0) \
        .click() \
        .perform()

    print(slider.get_attribute("value"))

    #         getActions().moveToElement(slider)
    #                 .moveByOffset(sliderWidth * 2 / 10, 0)
    #                 .click()
    #                 .perform();
    #
    #         System.out.println(slider.getAttribute("value"));
    #
    time.sleep(3)


def test_key_actions(driver):
    go_to_web_form(driver)
    text_area = driver.find_element(By.NAME, "my-textarea")

    ActionChains(driver) \
        .click(text_area) \
        .key_down(Keys.SHIFT) \
        .send_keys("abcDe") \
        .key_up(Keys.SHIFT) \
        .perform()
    #         getActions().click(textArea)
    #                 .keyDown(Keys.SHIFT)
    #                 .sendKeys("abcDe")
    #                 .keyUp(Keys.SHIFT)
    #                 .perform();
    #
    assert text_area.get_attribute("value") == "ABCDE"
    time.sleep(5)


def test_drag_and_drop(driver):
    go_to_drag_and_drop(driver)
    test1 = driver.find_element(By.ID, "test1")

    ActionChains(driver) \
        .click_and_hold(test1) \
        .move_by_offset(100, 50) \
        .pause(1) \
        .move_by_offset(100, 50) \
        .release() \
        .perform()

    #         getActions().clickAndHold(test1)
    #                 .moveByOffset(100, 50)
    #                 .pause(1000)
    #                 .moveByOffset(100, 50)
    #                 .release()
    #                 .perform();
    time.sleep(5)


def test_drag_and_drop_by(driver):
    go_to_drag_and_drop(driver)

    test1 = driver.find_element(By.ID, "test1")

    ActionChains(driver) \
        .drag_and_drop_by_offset(test1, 200, 400) \
        .perform()

    #         getActions()
    #                 .dragAndDropBy(test1, 200, 400)
    #                 .perform();
    time.sleep(5)


def test_drag_and_drop_to_element(driver):
    go_to_drag_and_drop(driver)
    test1 = driver.find_element(By.ID, "test1")
    print(test1.location)

    test4 = driver.find_element(By.ID, "test4")
    ActionChains(driver) \
        .drag_and_drop(test1, test4) \
        .perform()

    print(test1.location)
    assert (test4.location == test1.location)
    time.sleep(5)


# 🔥 Итог
#
# ✔ Java dragAndDrop → Python drag_and_drop
# ✔ getLocation() → .location
# ✔ Assert → assert
# ✔ логика полностью совпадает


def test_color(driver):
    go_to_web_form(driver)

    color_picker = driver.find_element(By.NAME, "my-colors")
    print(color_picker.get_attribute("value"))

    color_picker.click()

    driver.execute_script(
        "arguments[0].value = '#ff0000';", color_picker
    )

    # ActionChains(driver) \
    #     .send_keys(Keys.TAB, Keys.TAB) \
    #     .pause(0.5) \
    #     .send_keys("255") \
    #     .send_keys(Keys.TAB) \
    #     .pause(0.5) \
    #     .send_keys("0") \
    #     .send_keys(Keys.TAB) \
    #     .pause(0.5) \
    #     .send_keys("0") \
    #     .pause(0.5) \
    #     .send_keys(Keys.ENTER) \
    #     .perform()

    color = color_picker.get_attribute("value")
    print(color)

    assert color == "#ff0000" == color

    time.sleep(2)
