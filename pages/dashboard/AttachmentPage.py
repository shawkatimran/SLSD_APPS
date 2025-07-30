from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException, NoSuchElementException, StaleElementReferenceException
from pages.BasePage import BasePage
import time

class AttachmentPage(BasePage):
    # Locators for file inputs
    FILE_INPUTS_WITH_FILE_PREFIX = (By.CSS_SELECTOR, 'input[type="file"][id^="file"]')
    ALL_FILE_INPUTS = (By.CSS_SELECTOR, 'input[type="file"]')
    IFRAMES = (By.TAG_NAME, 'iframe')

    def check_for_iframes(self):
        """Check if there are any iframes on the page"""
        try:
            iframes = self.driver.find_elements(*self.IFRAMES)
            print(f"Found {len(iframes)} iframes on the page.")
            return iframes
        except Exception as e:
            print(f"Error checking for iframes: {e}")
            return []

    def process_attachments_in_current_context(self, file_path):
        """Process attachments in the current driver context (main page or iframe)"""
        success_count = 0
        
        try:
            # Wait for page to be ready
            time.sleep(2)
            
            # Find file input elements with flexible approach
            file_inputs = self.driver.find_elements(*self.FILE_INPUTS_WITH_FILE_PREFIX)
            
            if not file_inputs:
                print("No file inputs with IDs starting with 'file'. Trying all file inputs...")
                file_inputs = self.driver.find_elements(*self.ALL_FILE_INPUTS)
            
            if not file_inputs:
                print("No file inputs found in current context.")
                return False
                
            print(f"Found {len(file_inputs)} attachment fields in current context")
            
            # Process each file input
            for i, input_element in enumerate(file_inputs, 1):
                if self.upload_to_file_input(input_element, file_path, i, len(file_inputs)):
                    success_count += 1
                    time.sleep(3)  # Wait between uploads
            
            print(f"Successfully uploaded {success_count} out of {len(file_inputs)} attachments")
            return success_count > 0
            
        except Exception as e:
            print(f"Error processing attachments in current context: {e}")
            return False

    def upload_to_file_input(self, input_element, file_path, index, total):
        """Upload file to a specific file input element"""
        try:
            input_id = input_element.get_attribute('id') or f"unnamed-input-{index}"
            print(f"Processing attachment field {index}/{total}: ID={input_id}")
            
            # Make sure element is interactable
            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", input_element)
            time.sleep(1)
            self.driver.execute_script("arguments[0].style.display = 'block'; arguments[0].style.visibility = 'visible';", input_element)
            time.sleep(1)
            
            # Upload the file
            input_element.send_keys(file_path)
            print(f"Successfully uploaded file to field {index}")
            return True
            
        except StaleElementReferenceException:
            print(f"Element became stale, page may have changed.")
            return False
            
        except Exception as e:
            print(f"Error uploading to field {index}: {e}")
            return False

    def process_attachments_in_iframe(self, iframe, file_path, iframe_index, total_iframes):
        """Process attachments within a specific iframe"""
        try:
            print(f"Switching to iframe {iframe_index}/{total_iframes}")
            self.driver.switch_to.frame(iframe)
            
            # Process attachments in this iframe
            result = self.process_attachments_in_current_context(file_path)
            if result:
                print("Successfully processed attachments in iframe")
            
            # Switch back to main content
            self.driver.switch_to.default_content()
            return result
            
        except Exception as e:
            print(f"Error working with iframe {iframe_index}: {e}")
            # Make sure we get back to the main window
            self.driver.switch_to.default_content()
            return False

    def upload_attachments(self, file_path=r"E:\AUTOMATION_TESTING\SLSD_APPLICATIONS\TEST_DATA\Test_Doc.pdf"):
        """Main method to upload attachments to all available file inputs"""
        try:
            print("Starting attachment upload process...")
            
            # Check for iframes first
            iframes = self.check_for_iframes()
            
            if iframes:
                print(f"Checking for file inputs in {len(iframes)} iframes...")
                
                # Try checking each iframe for file inputs
                for i, iframe in enumerate(iframes):
                    self.process_attachments_in_iframe(iframe, file_path, i+1, len(iframes))
            
            # Check for attachments in the main page context
            print("Checking for attachments in main page context...")
            main_result = self.process_attachments_in_current_context(file_path)
            
            print("Attachment upload process completed")
            return True
            
        except Exception as e:
            print(f"Critical error in attachment upload: {e}")
            # Try to restore default content in case we're stuck in an iframe
            try:
                self.driver.switch_to.default_content()
            except:
                pass
            return False

    def upload_attachments_with_custom_path(self, file_path):
        """Upload attachments with a custom file path"""
        return self.upload_attachments(file_path)

    def upload_multiple_attachments(self, file_paths_list):
        """Upload multiple different files to different attachment fields"""
        try:
            print("Starting multiple attachment upload process...")
            success_count = 0
            
            # Get all file inputs
            file_inputs = self.driver.find_elements(*self.FILE_INPUTS_WITH_FILE_PREFIX)
            if not file_inputs:
                file_inputs = self.driver.find_elements(*self.ALL_FILE_INPUTS)
            
            if not file_inputs:
                print("No file inputs found for multiple upload.")
                return False
            
            print(f"Found {len(file_inputs)} file inputs for {len(file_paths_list)} files")
            
            # Upload files to available inputs
            for i, file_path in enumerate(file_paths_list):
                if i < len(file_inputs):
                    if self.upload_to_file_input(file_inputs[i], file_path, i+1, len(file_paths_list)):
                        success_count += 1
                        time.sleep(3)
                else:
                    print(f"No more file inputs available for file {i+1}")
                    break
            
            print(f"Successfully uploaded {success_count} out of {len(file_paths_list)} files")
            return success_count > 0
            
        except Exception as e:
            print(f"Error in multiple attachment upload: {e}")
            return False

    def verify_attachments_uploaded(self):
        """Verify that attachments have been uploaded successfully"""
        try:
            # Look for success indicators or filled file inputs
            file_inputs = self.driver.find_elements(*self.ALL_FILE_INPUTS)
            uploaded_count = 0
            
            for input_element in file_inputs:
                try:
                    # Check if the input has a value (file selected)
                    value = input_element.get_attribute('value')
                    if value and value.strip():
                        uploaded_count += 1
                except:
                    continue
            
            print(f"Verified {uploaded_count} attachments uploaded")
            return uploaded_count > 0
            
        except Exception as e:
            print(f"Error verifying attachments: {e}")
            return False

    def clear_all_attachments(self):
        """Clear all uploaded attachments"""
        try:
            file_inputs = self.driver.find_elements(*self.ALL_FILE_INPUTS)
            cleared_count = 0
            
            for input_element in file_inputs:
                try:
                    # Clear the file input
                    input_element.clear()
                    cleared_count += 1
                except:
                    continue
            
            print(f"Cleared {cleared_count} attachment fields")
            return cleared_count > 0
            
        except Exception as e:
            print(f"Error clearing attachments: {e}")
            return False
