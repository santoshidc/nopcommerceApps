import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
import time
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    '''baseURL = "https://admin-demo.nopcommerce.com/"
    username = "admin@yourstore.com"
    password = "admin" '''

    # Below reading from config.ini file
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    #def test_homePageTitle(self): # if webdriver needs to use
        #self.driver = webdriver.Chrome()

    @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("******************** Test_001_Login***************")
        self.logger.info("*****************Verifying Home Page Title***************")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        act_title = self.driver.title

        if act_title == "Your store. Login":
            self.logger.info("******************Home Page Title is TC is PASS!******************")
            self.driver.close()
            assert True
        else:
            self.logger.error("******************Home Page Title is TC is FAILED!******************")
            self.driver.save_screenshot(".\\Screenshots\\test_homePageTitle.png")
            self.driver.close()
            assert False

    #def test_login(self):  # if webdriver needs to use
        #self.driver = webdriver.Chrome()
    @pytest.mark.regression
    @pytest.mark.sanity
    def test_login(self, setup):
        self.logger.info("************************Verifying Login Test******************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        time.sleep(3)


        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("************************ Login Test PASSED!************************")
            self.lp.clickLogout()
            self.driver.close()
            assert True
        else:
            self.logger.error("********************* Logging Test FAILED!**********************")
            self.driver.save_screenshot(".\\Screenshots\\test_login.png")
            time.sleep(2)
            self.lp.clickLogout()
            self.driver.close()
            assert False



