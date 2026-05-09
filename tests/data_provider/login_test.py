import pytest

@pytest.mark.parametrize("username,password", [
    ("user1", "pass1"),
    ("user2", "pass2"),
    ("invalid", "wrong")
])
def test_login(username, password):
    print(username, password)