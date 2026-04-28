import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

input_name_locator = (By.ID, "firstName")
input_lastname_locator = (By.ID, "lastName")
input_email_locator = (By.ID, "userEmail")
radio_button_female_gender_locator = (By.XPATH, "//input[@value='Female']")
radio_button_f_gender_locator = (By.ID, "gender-radio-2")
radio_button_gender_locator = lambda gender: (By.XPATH, f"//input[@type ='radio' and @value='{gender}']")
# (By.XPATH, "//input[@type ='radio' and @value='Female']")
input_phone_number_locator = (By.ID, "userNumber")
input_data_of_birth_picker = (By.ID, "dateOfBirthInput")
select_month_of_birth_locator = lambda month: (By.XPATH, f"//select/option[contains(text(), '{month}')]")
select_year_of_birth_locator = lambda year: (By.XPATH, f"//select/option[contains(text(), '{year}')]")
select_day_of_birth_locator = (By.XPATH, "//div[@aria-label='Choose Monday, March 25th, 2002']")
select_hobbies_checkbox_locator = lambda hobby: (By.XPATH, f"//div[./label[text()='{hobby}']]/input")
input_subjects_locator = (By.ID, "subjectsInput")
select_subjects_list = (By.XPATH, "//div[@role='option' and contains(text(), 'Computer Science')]")
input_upload_picture = (By.ID, "uploadPicture")
input_current_address =(By.ID, "currentAddress")
select_state = (By.XPATH, "//div[@id='state']")
# select_state_list = lambda state: (By.XPATH, f"//div[@role='option' and contains(text(), '{state}')]")
select_state_list =  (By.XPATH, f"//div[@role='option' and contains(text(), 'Haryana')]")
select_city = (By.XPATH, "//div[@id='city']")
select_city_list =  (By.XPATH, f"//div[@role='option' and contains(text(), 'Panipat')]")
submit_button = (By.ID, "submit")
modal_title = (By.ID, "example-modal-sizes-title-lg")


list_of_hobbies = ["Sports", "Reading", "Music"]
def set_hobbies(driver: WebDriver, hobbies: list[str]):
    """
    Installing checkboxes
    :param driver: WebDriver
    :param hobbies: ["Sports", "Reading", "Music"]
    :return: None
    """
    for hobby in hobbies:
     driver.find_element(*select_hobbies_checkbox_locator(hobby = hobby)).click()

list_of_states = ["NCR", "Uttar Pradesh", "Haryana", "Rajasthan"]
# def set_states(driver: WebDriver, states: list[str]):
#     """
#     Installing checkboxes
#     :param driver: WebDriver
#     :param states: ["NCR", "Uttar Pradesh", "Haryana", "Rajasthan"]
#     :return: None
#     """
#     for state in states:
#      driver.find_element(*select_state_list(state = state)).click()



def test_demo():
    print("Attempting to open Chrome...")

    driver = webdriver.Chrome()

    try:
        # Открытие страницы
        print("Открытие тестовой страницы (https://demoqa.com/automation-practice-form)...")
        driver.get("https://demoqa.com/automation-practice-form")
        time.sleep(3)

        driver.find_element(*input_name_locator).send_keys("Anna")
        # time.sleep(3)
        driver.find_element(*input_lastname_locator).send_keys("Swan")
        # time.sleep(3)
        driver.find_element(*input_email_locator).send_keys("copif22224@spotshops.com")
        # time.sleep(3)
        driver.find_element(*radio_button_gender_locator(gender="Female")).click()
        # time.sleep(3)
        driver.find_element(*input_phone_number_locator).send_keys()
        time.sleep(2)
        phone = generate_phone_number()
        driver.find_element(*input_phone_number_locator).send_keys(phone)
        time.sleep(3)

        driver.find_element(*input_data_of_birth_picker).click()
        time.sleep(3)
        driver.find_element(*select_month_of_birth_locator(month="March")).click()
        time.sleep(3)
        driver.find_element(*select_year_of_birth_locator(year=2002)).click()
        time.sleep(3)
        driver.find_element(*select_day_of_birth_locator).click()
        time.sleep(3)

        # driver.find_element(*select_hobbies_checkbox_locator(hobby = "Music")).click()

        driver.find_element(*input_subjects_locator).send_keys("Co")
        time.sleep(3)
        driver.find_element(*select_subjects_list).click()
        time.sleep(3)
        set_hobbies(driver = driver,hobbies= list_of_hobbies)
        time.sleep(5)
        driver.find_element(*input_upload_picture).send_keys( r"C:\Users\kongo\OneDrive\Рабочий стол\easter.jpg")
        time.sleep(3)
        driver.find_element(*input_current_address).send_keys(r"73 Njdhe St., Constantinople")
        time.sleep(5)

        # state = driver.find_element(*select_state)
        # driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", state)
        # driver.execute_script("arguments[0].scrollIntoView(true);", state)
        # state.click()
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # set_states(driver = driver,states= list_of_states)
        time.sleep(3)
        driver.find_element(*select_state).click()
        time.sleep(3)
        driver.find_element(*select_state_list).click()
        time.sleep(5)
        driver.find_element(*select_city).click()
        time.sleep(3)
        driver.find_element(*select_city_list).click()
        time.sleep(5)
        driver.find_element(*submit_button).click()
        time.sleep(3)

        success_message = driver.find_element(*modal_title)
        assert "Thanks for submitting the form" in success_message.text.strip()




    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        print("Закрытие браузера...")
        driver.quit()


import random


def generate_phone_number():
    return str(random.randint(1000000000, 9999999999))

# def generate_phone():
#     return "+374" + str(random.randint(10000000, 99999999))
# print(generate_phone())


# setTimeout(() => {debugger; }, 3000);