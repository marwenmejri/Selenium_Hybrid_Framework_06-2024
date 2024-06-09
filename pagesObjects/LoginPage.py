from selenium.webdriver.common.by import By
# from selenium.webdriver import Chrome
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time


class LoginPage:
    username_by_id_locator = 'Email'

    def __init__(self, driver):
        self.driver = driver

    def set_username(self, username):
        self.driver.find_element(by=By.ID, value=self.username_by_id_locator).clear()
        self.driver.find_element(by=By.ID, value=self.username_by_id_locator).send_keys(username)

    def set_password(self, password):
        self.driver.find_element(by=By.ID, value="Password").clear()
        self.driver.find_element(by=By.ID, value="Password").send_keys(password)

    def login(self):
        self.driver.find_element(by=By.TAG_NAME, value="button").click()

    def logout(self):
        self.driver.find_element(by=By.XPATH, value="//a[normalize-space()='Logout']").click()


# if __name__ == '__main__':
#     driver1 = Chrome(service=Service(ChromeDriverManager().install()))
#     driver1.maximize_window()
#     driver1.implicitly_wait(time_to_wait=5)
#     url = 'https://admin-demo.nopcommerce.com/login'
#     driver1.get(url=url)
#
#     lp = LoginPage(driver=driver1)
#     lp.set_username(username='admin@yourstore.com')
#     lp.set_password(password='admin')
#     lp.login()
#     lp.logout()
#     driver1.quit()
