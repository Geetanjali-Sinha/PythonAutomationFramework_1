import allure
from selenium import webdriver
import pytest
from pages.loginPage import LoginPage
from pages.homePage import HomePage
from utils import utils as utils
import allure
import moment

@pytest.mark.usefixtures("test_setup")
class TestLogin():
  #  @pytest.fixture(scope="class")
 #   def test_setup(self):
 #       global driver
 #       driver=webdriver.Chrome(executable_path="C:/Users/Geetanjali/PycharmProjects/AutomationFramework_1/drivers/chromedriver.exe")
    #    driver.implicitly_wait(5)
     #   driver.maximize_window()
      #  yield
       # driver.close()
        #driver.quit()
        #print("Test Completed")

    #def test_login(self, test_setup):
    def test_login(self):
        driver = self.driver
        driver.get(utils.URL)
        #driver.get("https://opensource-demo.orangehrmlive.com")

        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        #login.enter_username("Admin")
        login.enter_password(utils.PASSWORD)
        #login.enter_password("admin123")
        login.click_login()


        #driver.find_element_by_id("txtUsername").send_keys("Admin")
        #driver.find_element_by_id("txtPassword").send_keys("admin123")
        #driver.find_element_by_id("btnLogin").click()

    #def test_logout(self, test_setup):
    def test_logout(self):
        try:
            driver = self.driver
            homepage = HomePage(driver)
            homepage.click_welcome()
            homepage.click_logout()
            x = driver.title
            assert x == "OrangeHRM"

        except AssertionError as error:
            print("Assertion error occured")
            print(error)
            currTime = moment.now().strftime("%d-%m-%y_%H-%M-%S")
            testName = utils.whoami()
            screenshotName = testName+"_"+currTime
            # screenshotName = "screenshot_"+currTime
            allure.attach(self.driver.get_screenshot_as_png(), name="screenshotName",
                          attachment_type=allure.attachment_type.PNG)
            raise

        except:
            print("There was an exception")
            # raise

        else:
            print("No exception occurred")

        finally:
            print("I am inside finally block")

        #driver.find_element_by_id("welcome").click()
        #driver.find_element_by_link_text("Logout").click()
