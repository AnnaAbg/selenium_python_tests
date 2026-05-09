import pytest

@pytest.fixture(params=[
    ("user1", "pass1"),
    ("user2", "pass2")
])
def login_data(request):
    return request.param

def test_login(login_data):
    username, password = login_data
    print(username, password)

import pytest

# Define the data sets directly in the decorator
@pytest.mark.parametrize("username, password, expected", [
    ("admin", "password123", True),
    ("user1", "wrongPass", False),
    ("guest", "guest123", True)
])
def test_login(username, password, expected):
    print(f"Testing {username} with {password}")
    # Your assertion logic here
    assert True == expected

# | Feature             | Java (TestNG) | Python (pytest) |
# | ------------------- | ------------- | --------------- |
# | Встроенный механизм | @DataProvider | @pytest.mark.parametrize |
# | Простота            | сложнее       | проще           |
# | Гибкость            | высокая       | очень высокая   |
# | Читаемость          | средняя       | высокая         |


# Feature,               Java (TestNG),                             Python (Pytest)
# Annotation/Decorator,  @DataProvider,                          pytest.mark.parametrize
# Data Format,           Object[][] or Iterator,                 List of tuples or lists
# Code Location,         Often a separate method,                Usually directly on the test
# Flexibility,           Strong type safety,                     Highly dynamic and concise