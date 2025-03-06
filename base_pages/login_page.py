from selenium.webdriver.common.by import By

class Login_Page:
    usernameId = "user-name"
    passwordId = "password"
    btnCss = "input[type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, self.usernameId).clear()
        self.driver.find_element(By.ID, self.usernameId).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, self.passwordId).clear()
        self.driver.find_element(By.ID, self.passwordId).send_keys(password)

    def push_login_button(self):
        self.driver.find_element(By.CSS_SELECTOR, self.btnCss).click()