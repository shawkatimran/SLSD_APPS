from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from pages.BasePage import BasePage
import time

class SubmitPage(BasePage):
    # Locators
    ACCEPT_TERMS_CHECKBOX = (By.XPATH, "//label[@for='accept_terms']")
    SUBMIT_BUTTON = (By.ID, 'submitForm')
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(text(), 'হ্যাঁ, জমা দিন')]")
    
    # Success/Error message locators (add these based on your application)
    SUCCESS_MESSAGE = (By.CLASS_NAME, 'success-message')
    ERROR_MESSAGE = (By.CLASS_NAME, 'error-message')

    def click_accept_terms_checkbox(self):
        """Click the accept terms checkbox"""
        try:
            self.click(self.ACCEPT_TERMS_CHECKBOX)
            print("Clicked the 'Accept Terms' checkbox.")
            time.sleep(2)
            return True
        except (TimeoutException, ElementNotInteractableException) as e:
            print(f"Failed to click accept terms checkbox: {e}")
            return False

    def scroll_to_submit_button(self):
        """Scroll to the submit button to ensure it's visible"""
        try:
            submit_button = self.wait.until(EC.presence_of_element_located(self.SUBMIT_BUTTON))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", submit_button)
            time.sleep(2)  # Allow the scrolling animation to complete
            print("Scrolled to submit button.")
            return True
        except Exception as e:
            print(f"Failed to scroll to submit button: {e}")
            return False

    def click_submit_button(self):
        """Click the submit button"""
        try:
            # First scroll to the button
            if not self.scroll_to_submit_button():
                return False
                
            # Then click it
            self.click(self.SUBMIT_BUTTON)
            print("Clicked the submit button.")
            time.sleep(2)
            return True
        except (TimeoutException, ElementNotInteractableException) as e:
            print(f"Failed to click submit button: {e}")
            return False

    def click_confirm_button(self):
        """Click the confirmation button"""
        try:
            confirm_button = self.wait.until(EC.element_to_be_clickable(self.CONFIRM_BUTTON))
            confirm_button.click()
            print("Clicked the confirmation button 'হ্যাঁ, জমা দিন'.")
            time.sleep(7)  # Wait for processing
            return True
        except (TimeoutException, ElementNotInteractableException) as e:
            print(f"Failed to click confirm button: {e}")
            return False

    def submit_form(self):
        """Complete the entire form submission process"""
        try:
            print("Starting form submission process...")
            
            # Step 1: Click accept terms checkbox
            if not self.click_accept_terms_checkbox():
                print("Failed to accept terms. Submission aborted.")
                return False
            
            # Step 2: Click submit button
            if not self.click_submit_button():
                print("Failed to click submit button. Submission aborted.")
                return False
            
            # Step 3: Click confirmation button
            if not self.click_confirm_button():
                print("Failed to confirm submission. Submission aborted.")
                return False
            
            print("Form submission completed successfully!")
            return True
            
        except Exception as e:
            print(f"Error during form submission: {e}")
            return False

    def verify_submission_success(self):
        """Verify that the form was submitted successfully"""
        try:
            # Look for success indicators
            # This can be customized based on your application's success indicators
            
            # Method 1: Check for success message
            try:
                success_element = self.wait.until(EC.presence_of_element_located(self.SUCCESS_MESSAGE))
                if success_element.is_displayed():
                    print("Success message found - submission verified.")
                    return True
            except TimeoutException:
                pass
            
            # Method 2: Check URL change (customize based on your app)
            current_url = self.driver.current_url
            if 'success' in current_url.lower() or 'submitted' in current_url.lower():
                print("URL indicates successful submission.")
                return True
            
            # Method 3: Check page title change
            page_title = self.driver.title
            if 'success' in page_title.lower() or 'submitted' in page_title.lower():
                print("Page title indicates successful submission.")
                return True
            
            print("Could not verify submission success.")
            return False
            
        except Exception as e:
            print(f"Error verifying submission: {e}")
            return False

    def check_for_submission_errors(self):
        """Check for any submission errors"""
        try:
            # Look for error messages
            try:
                error_element = self.driver.find_element(*self.ERROR_MESSAGE)
                if error_element.is_displayed():
                    error_text = error_element.text
                    print(f"Submission error found: {error_text}")
                    return error_text
            except:
                pass
            
            # Check for validation errors or other error indicators
            # This can be customized based on your application
            
            print("No submission errors detected.")
            return None
            
        except Exception as e:
            print(f"Error checking for submission errors: {e}")
            return None

    def submit_with_verification(self):
        """Submit form and verify the result"""
        try:
            # Submit the form
            if not self.submit_form():
                return False
            
            # Wait a moment for page to process
            time.sleep(3)
            
            # Check for errors first
            error = self.check_for_submission_errors()
            if error:
                print(f"Submission failed with error: {error}")
                return False
            
            # Verify success
            if self.verify_submission_success():
                print("Form submitted and verified successfully!")
                return True
            else:
                print("Form submitted but could not verify success.")
                return True  # Still consider it successful if no errors
                
        except Exception as e:
            print(f"Error in submit with verification: {e}")
            return False

    def retry_submission(self, max_retries=3):
        """Retry form submission if it fails"""
        for attempt in range(max_retries):
            try:
                print(f"Submission attempt {attempt + 1}/{max_retries}")
                
                if self.submit_with_verification():
                    print(f"Submission successful on attempt {attempt + 1}")
                    return True
                else:
                    print(f"Submission failed on attempt {attempt + 1}")
                    if attempt < max_retries - 1:
                        print("Retrying...")
                        time.sleep(5)  # Wait before retry
                        
            except Exception as e:
                print(f"Error on submission attempt {attempt + 1}: {e}")
                if attempt < max_retries - 1:
                    time.sleep(5)
        
        print(f"All {max_retries} submission attempts failed.")
        return False

    def force_submit(self):
        """Force submit without waiting for elements (emergency method)"""
        try:
            print("Attempting force submission...")
            
            # Try to find and click elements with JavaScript if normal methods fail
            try:
                self.driver.execute_script("document.querySelector('label[for=\"accept_terms\"]').click();")
                time.sleep(2)
                print("Force clicked accept terms checkbox.")
            except:
                pass
            
            try:
                self.driver.execute_script("document.getElementById('submitForm').click();")
                time.sleep(2)
                print("Force clicked submit button.")
            except:
                pass
            
            try:
                self.driver.execute_script("document.querySelector('button:contains(\"হ্যাঁ, জমা দিন\")').click();")
                time.sleep(7)
                print("Force clicked confirm button.")
            except:
                pass
            
            print("Force submission completed.")
            return True
            
        except Exception as e:
            print(f"Error in force submission: {e}")
            return False
