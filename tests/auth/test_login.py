from pages.auth.LoginPage import LoginPage
from config import LOGIN_PAGE_URL
from drivers import get_chrome_driver

def test_valid_login(driver):
    driver.get("https://www.google.com")
    

    #  stay for a while to see the page
    driver.implicitly_wait(10)

    # login_page.login("admin", "admin123")






