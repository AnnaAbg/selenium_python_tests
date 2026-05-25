import pytest


# Syntax: @pytest.mark.parametrize("arg1, arg2", [(val1, val2), (val3, val4)])
@pytest.mark.parametrize("username, password", [
    ("standard_user", "secret_sauce"),
    ("locked_out_user", "secret_sauce"),
    ("problem_user", "secret_sauce")
])
def test_login(username, password):
    print(f"Testing login for: {username}")
    # Your Selenium/Automation logic here
    assert username != ""

# Feature,               Python (pytest),                           Java (TestNG)
# Declaration,     @pytest.mark.parametrize,                 @DataProvider method + @Test
# Data Format,     List of tuples or lists,                 2D Object array (Object[][])
# Location,       Usually directly above the test,           Can be in the same class or a different one
# Readability,     Very high for small sets,               Better for complex/large data logic
# Execution,       Creates a unique test ID for each row,    Creates a unique test result for each row
