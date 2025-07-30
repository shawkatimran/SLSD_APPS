import pytest

from drivers.google_chrome_driver import get_chrome_driver
# Removed unused imports



@pytest.fixture
def driver():
    driver = get_chrome_driver(headless=False)
    print("Driver initialized")
    yield driver
    driver.quit()
