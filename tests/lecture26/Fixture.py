import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver # This provides the driver to the test
    driver.quit() # This runs AFTER the test finishes (Teardown)

def test_example(driver): # The driver is injected automatically
    driver.get("https://jenkins.io")
    assert "Jenkins" in driver.title



# vs Java
# Feature,Python (Pytest Fixture),Java (TestNG Annotations)
# Dependency Injection,Yes. You pass driver as a parameter to the test function.,No. The test method is usually empty-parameter; it uses the class field.
# Setup/Teardown Location,"Both are in the same function, separated by yield.",Split into two different methods with different annotations.
# Keyword for Setup,@pytest.fixture,@BeforeMethod (or @BeforeEach in JUnit).
# Keyword for Teardown,Code after yield,@AfterMethod (or @AfterEach in JUnit).