import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from common.jenkins_utils import login, logout, clear_data
from common.order_utils import reorder_items_by_dependency
from common.project_utils import get_browser, get_options, get_url


@pytest.fixture(scope="function")
def browser(request):
    get_browser()

    dependency_marker = request.node.get_closest_marker("dependency")
    depends = dependency_marker.kwargs.get("depends") if dependency_marker else None
    if not depends:
        print("\nclearing data")
        clear_data()

    options = webdriver.ChromeOptions()
    for option in get_options():
        options.add_argument(option)
    print("opening browser")
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(5)

    print("getting page")
    driver.get(get_url())
    login(driver)
    try:
        yield driver
    finally:
        try:
            logout(driver)
        finally:
            driver.quit()


@pytest.hookimpl(trylast=True)
def pytest_collection_modifyitems(session, config, items):
    reorder_items_by_dependency(items)

#
# @pytest.fixture(scope="function")
# def login_admin(driver):
#     login(driver=driver, user_name="admin", password="12345")
#
# @pytest.fixture(scope="function")
# def folder(login_admin, driver):
#     ex_name_folder = "Test Folder"
#     driver.find_element(By.XPATH, "//a[contains(., 'New Item')]")
#     driver.find_element(By.XPATH, "//input[@id='name']").send_keys(
#         ex_name_folder
#     )
#     driver.find_element(By.XPATH, "//li//span[text()='Folder']").click()
#     driver.find_element(By.XPATH, "//button[@type='submit']").click()
#     driver.find_element("//button[@value='Save']").click()