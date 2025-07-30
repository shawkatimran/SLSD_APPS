# SLSD Apps Automation Testing Framework

A comprehensive Selenium-based automation testing framework for the SLSD (Service and Legal Support Department) government web application.

## 🚀 Project Overview

This project provides automated testing capabilities for the SLSD government portal, focusing on user authentication, dashboard functionality, and critical user workflows. The framework is built using Python, Selenium WebDriver, and pytest.

## 📁 Project Structure

```
├── drivers/                    # WebDriver management
│   ├── __init__.py
│   └── google_chrome_driver.py # Chrome driver configuration
├── pages/                      # Page Object Model (POM)
│   ├── __init__.py
│   ├── BasePage.py            # Base page class with common methods
│   ├── auth/                  # Authentication related pages
│   │   ├── __init__.py
│   │   └── LoginPage.py       # Login page implementation
│   └── dashboard/             # Dashboard related pages
│       └── __init__.py
├── tests/                     # Test cases
│   ├── __init__.py
│   ├── auth/                  # Authentication tests
│   │   ├── __init__.py
│   │   ├── test_login.py      # Login functionality tests
│   │   └── test_values.py     # Test data for auth tests
│   └── dashboard/             # Dashboard tests
│       └── __init__.py
├── config.py                  # Configuration settings
├── conftest.py               # pytest fixtures and setup
├── requirements.txt          # Python dependencies
└── README.md                # Project documentation
```

## 🛠️ Technologies Used

- **Python 3.x** - Programming language
- **Selenium WebDriver** - Browser automation
- **pytest** - Testing framework
- **Chrome WebDriver** - Browser driver
- **Page Object Model (POM)** - Design pattern for maintainable tests

## 📋 Prerequisites

- Python 3.8 or higher
- Google Chrome browser
- ChromeDriver (automatically managed)
- pip (Python package manager)

## ⚙️ Installation

1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd slsd-automation-testing
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install ChromeDriver (if not using webdriver-manager):**
   ```bash
   # On Ubuntu/Debian
   sudo apt install chromium-chromedriver
   
   # Or download manually from:
   # https://chromedriver.chromium.org/
   ```

## 🚦 Running Tests

### Run all tests:
```bash
pytest
```

### Run specific test modules:
```bash
# Run all authentication tests
pytest tests/auth/

# Run specific test file
pytest tests/auth/test_login.py

# Run specific test function
pytest tests/auth/test_login.py::test_valid_login
```

### Run with verbose output:
```bash
pytest -v
```

### Run in headless mode:
Edit `conftest.py` and change `headless=False` to `headless=True`

### Generate HTML report:
```bash
pytest --html=reports/report.html --self-contained-html
```

## 🔧 Configuration

### Environment Configuration (`config.py`)
```python
BASE_URL = "https://uat-slsd.mohpw.gov.bd"
LOGIN_PAGE_URL = "https://idp-slsd.mohpw.gov.bd/realms/slsd/protocol/openid-connect/auth?..."
```

### Driver Configuration
The Chrome driver is configured in `drivers/google_chrome_driver.py` with:
- Headless mode support
- Window size optimization
- Performance settings
- Security options

## 📝 Writing Tests

### Example Test Structure:
```python
def test_valid_login(driver):
    driver.get(BASE_URL)
    
    login_page = LoginPage(driver)
    login_page.login(username, password)
    
    # Add assertions here
    assert "dashboard" in driver.current_url
```

### Page Object Example:
```python
class LoginPage(BasePage):
    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//span[@class='dlsd-btn-text']")
    
    def login(self, username, password):
        self.send_keys(self.USERNAME_FIELD, username)
        self.send_keys(self.PASSWORD_FIELD, password)
        self.click(self.LOGIN_BUTTON)
```

## 🎯 Test Scenarios Covered

### Authentication Tests
- ✅ Valid user login
- ⏳ Invalid credentials handling
- ⏳ Password reset functionality
- ⏳ Session management

### Dashboard Tests
- ⏳ Dashboard loading
- ⏳ Navigation menu functionality
- ⏳ User profile management

## 🐛 Troubleshooting

### Common Issues:

1. **ChromeDriver not found:**
   ```bash
   # Install ChromeDriver
   sudo apt install chromium-chromedriver
   # Or use webdriver-manager (already in requirements.txt)
   ```

2. **Element not found:**
   - Check if page is fully loaded
   - Verify element selectors
   - Add explicit waits

3. **Test timeout:**
   - Increase page load timeout in driver configuration
   - Check network connectivity
   - Verify application availability

## 📊 Reporting

Test reports are generated in the `reports/` directory (ignored in git):
- HTML reports with screenshots
- JUnit XML reports for CI/CD integration
- Allure reports (if configured)

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/new-test`
3. Write tests following the existing patterns
4. Ensure all tests pass: `pytest`
5. Commit your changes: `git commit -m "Add new test feature"`
6. Push to the branch: `git push origin feature/new-test`
7. Submit a pull request

## 📈 Best Practices

- Use Page Object Model for maintainable tests
- Add explicit waits instead of `time.sleep()`
- Keep test data separate from test logic
- Use meaningful test and method names
- Add appropriate assertions
- Handle exceptions gracefully
- Keep tests independent and atomic

## 🔒 Security Notes

- Never commit real credentials
- Use environment variables for sensitive data
- Keep test data in separate files (ignored in git)
- Follow security best practices for web automation

## 📞 Support

For issues, questions, or contributions:
- Create an issue in the repository
- Contact the development team
- Check the troubleshooting section

## 📄 License

This project is proprietary and confidential. Unauthorized copying, modification, or distribution is prohibited.

---

**Note:** This is a government application testing framework. Ensure compliance with all security and privacy regulations when running tests.
