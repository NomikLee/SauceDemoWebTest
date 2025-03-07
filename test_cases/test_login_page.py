import pytest
from selenium.webdriver.common.by import By
from utilities.read_properties import Read_Config
from base_pages.login_page import Login_Page
from utilities.custom_log import Log_Maker

class Test_Login_Page:
    logger = Log_Maker.log_gen()

    def test_login_screen_correct(self, driver):
        self.logger.info("*************Test_Login_Page*************")
        self.logger.info("*************test_login_screen_correct*************")
        login_screen_title = "Swag Labs"
        driver.get(Read_Config.get_page_url())

        if driver.title != login_screen_title:
            driver.save_screenshot("./screenshots/test_login_screen_correct.png")
            self.logger.info("*************test_login_screen_correct title no matched*************")

        assert driver.title == login_screen_title
        self.logger.info("*************test_login_screen_correct title matched*************")

    def test_successful_login(self, driver):
        self.logger.info("*************test_successful_login*************")
        driver.get(Read_Config.get_page_url())
        self.login_page_do = Login_Page(driver)
        self.login_page_do.enter_username(Read_Config.get_username())
        self.login_page_do.enter_password(Read_Config.get_password())
        self.login_page_do.push_login_button()

        home_title = driver.find_element(By.CSS_SELECTOR, ".app_logo").text

        if home_title != "Swag Labs":
            driver.save_screenshot("./screenshots/test_successful_login.png")
            self.logger.info("*************test_successful_login title no matched*************")

        assert home_title == "Swag Labs"
        self.logger.info("*************test_successful_login title matched*************")

    @pytest.mark.parametrize(
        "fail_username, fail_password",
        [
            (Read_Config.get_invalid_username(), Read_Config.get_password()),
            (Read_Config.get_username(), "1111")
        ]
    )
    def test_login_fail(self, driver, fail_username, fail_password):
        self.logger.info("*************test_login_fail*************")
        driver.get(Read_Config.get_page_url())
        self.login_page_do = Login_Page(driver)
        self.login_page_do.enter_username(fail_username)
        self.login_page_do.enter_password(fail_password)
        self.login_page_do.push_login_button()
        fail_text = driver.find_element(By.CSS_SELECTOR, "h3[data-test = 'error']").text

        if fail_text != "Epic sadface: Username and password do not match any user in this service":
            driver.save_screenshot("./screenshots/test_login_fail.png")
            self.logger.info("*************test_login_fail message no matched*************")

        assert fail_text == "Epic sadface: Username and password do not match any user in this service"
        self.logger.info("*************test_login_fail message matched*************")

    def test_login_lock(self, driver):
        self.logger.info("*************test_login_lock*************")
        driver.get(Read_Config.get_page_url())
        self.login_page_do = Login_Page(driver)
        self.login_page_do.enter_username(Read_Config.get_locked_username())
        self.login_page_do.enter_password(Read_Config.get_password())
        self.login_page_do.push_login_button()
        fail_text = driver.find_element(By.CSS_SELECTOR, "h3[data-test = 'error']").text

        if fail_text != "Epic sadface: Sorry, this user has been locked out.":
            driver.save_screenshot("./screenshots/test_login_lock.png")
            self.logger.info("*************test_login_lock message no matched*************")

        assert fail_text == "Epic sadface: Sorry, this user has been locked out."
        self.logger.info("*************test_login_lock message matched*************")


    @pytest.mark.parametrize(
        "no_info_username, no_info_password",
        [
            ("", ""),
            (Read_Config.get_username(), ""),
            ("", Read_Config.get_password())
        ]
    )
    def test_login_no_info_give(self, driver, no_info_username, no_info_password):
        self.logger.info("*************test_login_no_info_give*************")
        driver.get(Read_Config.get_page_url())
        self.login_page_do = Login_Page(driver)
        self.login_page_do.enter_username(no_info_username)
        self.login_page_do.enter_password(no_info_password)
        self.login_page_do.push_login_button()
        fail_text = driver.find_element(By.CSS_SELECTOR, "h3[data-test = 'error']").text
        compare_text = ""
        compare_png_name = ""

        if no_info_username == "":
            compare_text = "Epic sadface: Username is required"
            compare_png_name = "Username"
        elif no_info_username != "" and no_info_password == "":
            compare_text = "Epic sadface: Password is required"
            compare_png_name = "Password"

        if fail_text != compare_text:
            driver.save_screenshot(f"./screenshots/test_login_no_info_give_{compare_png_name}_message_no_matched.png")
            self.logger.info("*************test_login_no_info_give message no matched*************")
            assert fail_text == compare_text

        self.logger.info("*************test_login_no_info_give message matched*************")
