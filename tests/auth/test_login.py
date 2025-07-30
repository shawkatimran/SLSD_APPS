from pages.auth.LoginPage import LoginPage
from config import LOGIN_PAGE_URL
from drivers import get_chrome_driver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException

def test_valid_login(driver):
    driver.get("https://uat-slsd.mohpw.gov.bd/")

    login_page = LoginPage(driver)
    login_page.login("01961627162", "123456aA@")
    time.sleep(5) 
 
    

    


   

    
    




