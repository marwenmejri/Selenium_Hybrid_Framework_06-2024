from pagesObjects.LoginPage import LoginPage
from utilities.customLogger import Logger
from utilities.read_properties import load_value, get_username


class Test001Login:
    # username = load_value(section='common info', option='username')  # 'admin@yourstore.com'
    baseURL = load_value(section='common info', option='baseURL')
    username = get_username()
    password = load_value(section='common info', option='password')
    logger = Logger.sample_logger()

    def test_verify_page_login(self, setup):
        self.logger.info('************** Test001Login Started *************')
        self.logger.info('************** test_verify_page_login Started *************')
        driver = setup
        driver.get(url=self.baseURL)
        if driver.title == "Your store. Login":
            self.logger.info('************** test_verify_page_login Passed *************')
            # driver.quit()
            assert True
        else:
            driver.save_screenshot("Screenshots/test_verify_login_page.png")
            self.logger.error('************** test_verify_page_login Failed *************')
            # driver.quit()
            assert False

    def test_login(self, setup):
        self.logger.info('************** test_login Started *************')
        driver = setup
        driver.get(url=self.baseURL)
        lp = LoginPage(driver=driver)
        lp.set_username(username=self.username)
        lp.set_password(password=self.password)
        lp.login()
        title = driver.title
        if title == "Dashboard / nopCommerce administration":
            lp.logout()
            # driver.quit()
            self.logger.info('************** test_login Passed *************')
            assert True
        else:
            driver.save_screenshot("Screenshots/test_login.png")
            # driver.quit()
            self.logger.error('************** test_login Failed *************')
            assert False

    def test_verify_page_login1(self, setup):
        self.logger.info('************** test_verify_page_login1 Started *************')
        driver = setup
        driver.get(url=self.baseURL)
        if driver.title == "Your store. Login":
            self.logger.info('************** test_verify_page_login1 Passed *************')
            # driver.quit()
            assert True
        else:
            driver.save_screenshot("Screenshots/test_verify_login_page1.png")
            self.logger.error('************** test_verify_page_login1 Failed *************')
            # driver.quit()
            assert False

    def test_login1(self, setup):
        self.logger.info('************** test_login1 Started *************')
        driver = setup
        driver.get(url=self.baseURL)
        lp = LoginPage(driver=driver)
        lp.set_username(username=self.username)
        lp.set_password(password=self.password)
        lp.login()
        title = driver.title
        if title == "Dashboard / nopCommerce administration":
            lp.logout()
            driver.quit()
            self.logger.info('************** test_login1 Passed *************')
            assert True
        else:
            driver.save_screenshot("Screenshots/test_login1.png")
            driver.quit()
            self.logger.error('************** test_login1 Failed *************')
            assert False
