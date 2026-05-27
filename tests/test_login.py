from pages.login_page import LoginPage
#Login Test
# Valid Login
def test_valid_login(driver):
    login = LoginPage(driver)
    login.open()

    login.enter_username("tomsmith")
    login.enter_password("SuperSecretPassword!")
    login.click_login()

    assert "secure" in login.get_message()

#Invalid password
def test_invalid_password(driver):
    login = LoginPage(driver)
    login.open()

    login.enter_username("tomsmith")
    login.enter_password("wrong")
    login.click_login()

    assert "invalid" in login.get_message()

#Invalid Username
def test_invalid_username(driver):
    login = LoginPage(driver)
    login.open()

    login.enter_username("wrong")
    login.enter_password("SuperSecretPassword!")
    login.click_login()

    assert "invalid" in login.get_message()

#Empty Login
def test_empty_login(driver):
    login = LoginPage(driver)
    login.open()

    login.click_login()

    assert "invalid" in login.get_message()

#Flow Test
#Logout flow
def test_logout(driver):
    login = LoginPage(driver)
    login.open()

    login.enter_username("tomsmith")
    login.enter_password("SuperSecretPassword!")
    login.click_login()

    login.logout()

    assert "login" in driver.current_url.lower()
    
#UI test
def test_ui_elements(driver):
    login = LoginPage(driver)
    login.open()

    assert driver.find_element("id", "username")
    assert driver.find_element("id", "password")
    assert driver.find_element("class name", "radius")

#Title test
def test_title(driver):
    login = LoginPage(driver)
    login.open()

    assert "the internet" in login.get_title()

#Edge test
#Special Characters
def test_special_chars(driver):
    login = LoginPage(driver)
    login.open()

    login.enter_username("@#$%")
    login.enter_password("@#$%")
    login.click_login()

    assert "invalid" in login.get_message()

#Long Input
def test_long_input(driver):
    login = LoginPage(driver)
    login.open()

    long_text = "a" * 200

    login.enter_username(long_text)
    login.enter_password(long_text)
    login.click_login()

    assert "invalid" in login.get_message()

#Multiple Attempts
def test_multiple_attempts(driver):
    login = LoginPage(driver)
    login.open()

    for i in range(3):
        login.login("wrong", "wrong")

        assert "invalid" in login.get_message()

        driver.get("https://the-internet.herokuapp.com/login")