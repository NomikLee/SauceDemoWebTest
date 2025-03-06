from selenium.webdriver.common.by import By
from utilities.read_properties import Read_Config
from base_pages.login_page import Login_Page

class Test_Login_Page:
    page_url = Read_Config.get_page_url()
    username = Read_Config.get_username()
    password = Read_Config.get_password()
    invalid_username = Read_Config.get_invalid_username()
    locked_username = Read_Config.get_locked_username()

    def test_login_screen_correct(self, driver):
        login_screen_title = "Swag Labs"
        driver.get(self.page_url)

        if driver.title != login_screen_title:
            driver.save_screenshot("./screenshots/test_login_screen_correct.png")
            print("*************test_login_screen_correct title no matched*************")

        assert driver.title == login_screen_title

        print("*************test_login_screen_correct title matched*************")

    def test_successful_login(self, driver):
        driver.get(self.page_url)
        self.login_page_do = Login_Page(driver)
        self.login_page_do.enter_username(self.username)
        self.login_page_do.enter_password(self.password)
        self.login_page_do.push_login_button()

        home_title = driver.find_element(By.CSS_SELECTOR, ".app_logo").text

        if home_title != "Swag Labs":
            driver.save_screenshot("./screenshots/test_successful_login.png")
            print("*************test_successful_login title no matched*************")

        assert home_title == "Swag Labs"

        print("*************test_successful_login title matched*************")
