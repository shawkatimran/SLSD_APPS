from pages.auth.LoginPage import LoginPage
from config import LOGIN_PAGE_URL
from drivers import get_chrome_driver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from config import BASE_URL
from tests.auth.test_values import login

def test_valid_login(driver):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(login["username"], login["password"])
    time.sleep(5) 
 
    

    


   

    
    




