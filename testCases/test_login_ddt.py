from pagesObjects.LoginPage import LoginPage
from utilities.customLogger import Logger
from utilities.json_data_utils import read_json_data
from utilities.read_properties import load_value, get_username


class Test002DDTLogin:
    baseURL = load_value(section='common info', option='baseURL')
    file_path = 'TestData/LoginData.json'
    logger = Logger.sample_logger()

    def test_login_ddt(self, setup):
        self.logger.info('************** Test002DDTLogin Started *************')
        self.logger.info('************** Test Login DDT Started *************')
        driver = setup
        driver.get(url=self.baseURL)
        lp = LoginPage(driver=driver)
        data = read_json_data(file_path=self.file_path)
        print(data)

        # Loop through all login scenarios
        iteration = 0
        for item in data:
            iteration += 1
            lp.set_username(username=item['username'])
            lp.set_password(password=item['password'])
            lp.login()
            title = driver.title
            if title == "Dashboard / nopCommerce administration":
                if item['exp'] == 'Pass':
                    lp.logout()
                    self.logger.info(f'************** Scenario {iteration} Passed *************')
                else:
                    driver.save_screenshot(f"Screenshots/Scenario_{iteration}.png")
                    self.logger.error(f'************** Scenario {iteration} Failed *************')
                    self.logger.error(f'************** Test Login DDT Failed *************')
                    assert False
            else:
                if item['exp'] == 'Pass':
                    driver.save_screenshot(f"Screenshots/Scenario_{iteration}.png")
                    self.logger.error(f'************** Scenario {iteration} Failed *************')
                    self.logger.error(f'************** Test Login DDT Failed *************')
                    assert False
                else:
                    self.logger.info(f'************** Scenario {iteration} Passed *************')
        self.logger.info(f'************** Test Login DDT Passed *************')
