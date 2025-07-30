from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from pages.BasePage import BasePage
import time

class RecipientPage(BasePage):
    # Locators for Add Recipient Info
    ADD_RECIPIENT_BUTTON = (By.ID, 'recipient_addMoreBtn')
    BRN_RADIO_BUTTON = (By.XPATH, '//label[@for="identification_brn" and contains(text(), "জন্ম নিবন্ধন")]')
    BRN_INPUT = (By.ID, 'verify_brn_no')
    DOB_INPUT = (By.ID, 'verify_brn_dob')
    VERIFY_BUTTON = (By.ID, 'verifyBRN')
    
    # Locators for Recipient Details
    RECIPIENT_NAME_BN = (By.ID, 'recipient_name_bn')
    RECIPIENT_NAME_EN = (By.ID, 'recipient_name_en')
    FATHER_NAME = (By.ID, 'recipient_father_name')
    MOTHER_NAME = (By.ID, 'recipient_mother_name')
    SPOUSE_NAME = (By.ID, 'recipient_spouse_name')
    NATIONALITY = (By.ID, 'recipient_nationality')
    
    # Contact Information
    RECIPIENT_MOBILE = (By.ID, 'recipient_mobile')
    RECIPIENT_EMAIL = (By.ID, 'recipient_email')
    RECIPIENT_TIN = (By.ID, 'recipient_tin_no')
    
    # Location Dropdowns
    RECIPIENT_DISTRICT_DROPDOWN = (By.ID, "recipient_present_district_id")
    RECIPIENT_THANA_DROPDOWN = (By.ID, "recipient_present_thana_id")
    
    # Address Checkbox
    RECIPIENT_SAME_ADDRESS_CHECKBOX = (By.XPATH, "//label[@for='recipient_is_pp_same_address' and contains(text(), 'স্থায়ী ও বর্তমান ঠিকানা একই')]")
    
    # File Upload
    RECIPIENT_SIGNATURE_INPUT = (By.ID, 'recipient_signature')
    RECIPIENT_PHOTO_INPUT = (By.ID, 'recipient_photo')
    CROP_IMAGE_BUTTON = (By.ID, 'cropImageBtn')
    
    # Save Buttons
    RECIPIENT_SAVE_INFO_BUTTON = (By.ID, 'recipient_saveInfo')
    NEXT_BUTTON = (By.XPATH, '//a[@class="next" and @href="#next"]')

    def click_add_recipient_button(self):
        """Click the add recipient button"""
        try:
            self.click(self.ADD_RECIPIENT_BUTTON)
            print("Clicked the 'আরও গ্রহীতার তথ্য যুক্ত করুন' button.")
            return True
        except (TimeoutException, ElementNotInteractableException) as e:
            print(f"Failed to click add recipient button: {e}")
            return False

    def select_brn_verification(self):
        """Select birth registration certificate for verification"""
        try:
            self.click(self.BRN_RADIO_BUTTON)
            print("Selected 'জন্ম নিবন্ধন' radio button.")
            return True
        except (TimeoutException, ElementNotInteractableException) as e:
            print(f"Failed to select BRN verification: {e}")
            return False

    def fill_brn_verification_details(self, brn_number, dob):
        """Fill BRN verification details"""
        try:
            # Fill BRN number
            self.send_keys(self.BRN_INPUT, brn_number)
            print(f"Entered BRN number: {brn_number}")
            
            # Fill date of birth
            self.send_keys(self.DOB_INPUT, dob)
            print(f"Entered date: {dob}")
            
            return True
        except (TimeoutException, ElementNotInteractableException) as e:
            print(f"Failed to fill BRN verification details: {e}")
            return False

    def click_verify_button(self):
        """Click the verify button"""
        try:
            self.click(self.VERIFY_BUTTON)
            print("Clicked the 'যাচাই করুন' button.")
            return True
        except (TimeoutException, ElementNotInteractableException) as e:
            print(f"Failed to click verify button: {e}")
            return False

    def fill_recipient_basic_info(self, name_bn, name_en, father_name, mother_name, spouse_name, nationality):
        """Fill recipient basic information"""
        try:
            # Fill recipient name in Bengali
            self.send_keys(self.RECIPIENT_NAME_BN, name_bn)
            print(f"Entered recipient name (Bengali): {name_bn}")
            
            # Fill recipient name in English
            self.send_keys(self.RECIPIENT_NAME_EN, name_en)
            print(f"Entered recipient name (English): {name_en}")
            
            # Fill father's name
            self.send_keys(self.FATHER_NAME, father_name)
            print(f"Entered father's name: {father_name}")
            
            # Fill mother's name
            self.send_keys(self.MOTHER_NAME, mother_name)
            print(f"Entered mother's name: {mother_name}")
            
            # Fill spouse name
            self.send_keys(self.SPOUSE_NAME, spouse_name)
            print(f"Entered spouse name: {spouse_name}")
            
            # Fill nationality
            self.send_keys(self.NATIONALITY, nationality)
            print(f"Entered nationality: {nationality}")
            
            return True
        except Exception as e:
            print(f"Failed to fill recipient basic info: {e}")
            return False

    def fill_recipient_contact_info(self, mobile, email, tin):
        """Fill recipient contact information"""
        try:
            # Fill mobile number
            mobile_element = self.wait.until(EC.element_to_be_clickable(self.RECIPIENT_MOBILE))
            mobile_element.click()
            print("Clicked on the mobile input field.")
            mobile_element.send_keys(mobile)
            print(f"Entered mobile number: {mobile}")
            
            # Fill email
            self.send_keys(self.RECIPIENT_EMAIL, email)
            print(f"Entered email: {email}")
            
            # Fill TIN number
            self.send_keys(self.RECIPIENT_TIN, tin)
            print(f"Entered TIN number: {tin}")
            
            return True
        except Exception as e:
            print(f"Failed to fill recipient contact info: {e}")
            return False

    def select_recipient_location(self, district, thana):
        """Select recipient district and thana"""
        try:
            # Select district
            district_dropdown = self.driver.find_element(*self.RECIPIENT_DISTRICT_DROPDOWN)
            district_select = Select(district_dropdown)
            district_select.select_by_visible_text(district)
            print(f"Selected district: {district}")
            time.sleep(3)
            
            # Select thana
            thana_dropdown = self.driver.find_element(*self.RECIPIENT_THANA_DROPDOWN)
            thana_select = Select(thana_dropdown)
            thana_select.select_by_visible_text(thana)
            print(f"Selected thana: {thana}")
            
            return True
        except Exception as e:
            print(f"Failed to select recipient location: {e}")
            return False

    def click_recipient_same_address_checkbox(self):
        """Click the same address checkbox for recipient"""
        try:
            checkbox = self.driver.find_element(*self.RECIPIENT_SAME_ADDRESS_CHECKBOX)
            checkbox.click()
            print("Clicked the checkbox 'স্থায়ী ও বর্তমান ঠিকানা একই'.")
            time.sleep(3)
            return True
        except Exception as e:
            print(f"Failed to click same address checkbox: {e}")
            return False

    def upload_recipient_signature(self, signature_path):
        """Upload recipient signature"""
        try:
            # Upload signature file
            signature_input = self.driver.find_element(*self.RECIPIENT_SIGNATURE_INPUT)
            signature_input.send_keys(signature_path)
            print(f"Signature uploaded: {signature_path}")
            
            # Click save button
            save_button = self.wait.until(EC.element_to_be_clickable(self.CROP_IMAGE_BUTTON))
            save_button.click()
            print("Signature saved.")
            time.sleep(2)
            
            return True
        except Exception as e:
            print(f"Failed to upload recipient signature: {e}")
            return False

    def upload_recipient_photo(self, photo_path):
        """Upload recipient photo"""
        try:
            # Upload photo file
            photo_input = self.driver.find_element(*self.RECIPIENT_PHOTO_INPUT)
            photo_input.send_keys(photo_path)
            print(f"Photo uploaded: {photo_path}")
            time.sleep(4)
            
            # Click save button
            save_button = self.wait.until(EC.element_to_be_clickable(self.CROP_IMAGE_BUTTON))
            save_button.click()
            print("Photo saved.")
            time.sleep(1)
            
            return True
        except Exception as e:
            print(f"Failed to upload recipient photo: {e}")
            return False

    def save_recipient_info(self):
        """Save recipient information"""
        try:
            save_button = self.wait.until(EC.element_to_be_clickable(self.RECIPIENT_SAVE_INFO_BUTTON))
            save_button.click()
            print("Recipient information saved.")
            time.sleep(5)
            return True
        except Exception as e:
            print(f"Failed to save recipient info: {e}")
            return False

    def click_next_button(self):
        """Click the next button to proceed"""
        try:
            next_button = self.wait.until(EC.element_to_be_clickable(self.NEXT_BUTTON))
            next_button.click()
            print("Next button clicked.")
            return True
        except Exception as e:
            print(f"Failed to click next button: {e}")
            return False

    def add_recipient_with_brn_verification(self, brn_data):
        """Add recipient info with BRN verification"""
        try:
            # Click add recipient button
            if not self.click_add_recipient_button():
                return False
                
            # Select BRN verification
            if not self.select_brn_verification():
                return False
                
            # Fill BRN verification details
            if not self.fill_brn_verification_details(brn_data['brn_number'], brn_data['dob']):
                return False
                
            # Click verify button
            if not self.click_verify_button():
                return False
                
            print("BRN verification completed successfully.")
            return True
            
        except Exception as e:
            print(f"Error in BRN verification: {e}")
            return False

    def fill_complete_recipient_details(self, basic_info, contact_info, location_info, file_paths):
        """Fill complete recipient details"""
        try:
            # Fill basic information
            if not self.fill_recipient_basic_info(**basic_info):
                return False
                
            # Fill contact information
            if not self.fill_recipient_contact_info(**contact_info):
                return False
                
            # Select location
            if not self.select_recipient_location(**location_info):
                return False
                
            # Click same address checkbox
            if not self.click_recipient_same_address_checkbox():
                return False
                
            # Upload signature
            if 'signature_path' in file_paths:
                if not self.upload_recipient_signature(file_paths['signature_path']):
                    return False
                    
            # Upload photo
            if 'photo_path' in file_paths:
                if not self.upload_recipient_photo(file_paths['photo_path']):
                    return False
                    
            # Save recipient info
            if not self.save_recipient_info():
                return False
                
            # Click next button
            if not self.click_next_button():
                return False
                
            print("Recipient details filled successfully.")
            return True
            
        except Exception as e:
            print(f"Error filling recipient details: {e}")
            return False

    def complete_recipient_process(self, brn_data, basic_info, contact_info, location_info, file_paths):
        """Complete the entire recipient process"""
        try:
            # Step 1: Add recipient with BRN verification
            if not self.add_recipient_with_brn_verification(brn_data):
                return False
                
            # Step 2: Fill complete recipient details
            if not self.fill_complete_recipient_details(basic_info, contact_info, location_info, file_paths):
                return False
                
            print("Complete recipient process finished successfully.")
            return True
            
        except Exception as e:
            print(f"Error in complete recipient process: {e}")
            return False

    def fill_recipient_details_only(self, basic_info, contact_info, location_info, file_paths):
        """Fill recipient details only (when BRN verification already done)"""
        try:
            # Fill basic information
            if not self.fill_recipient_basic_info(**basic_info):
                return False
                
            # Fill contact information
            if not self.fill_recipient_contact_info(**contact_info):
                return False
                
            # Select location
            if not self.select_recipient_location(**location_info):
                return False
                
            # Click same address checkbox
            if not self.click_recipient_same_address_checkbox():
                return False
                
            # Upload files
            if 'signature_path' in file_paths:
                if not self.upload_recipient_signature(file_paths['signature_path']):
                    return False
                    
            if 'photo_path' in file_paths:
                if not self.upload_recipient_photo(file_paths['photo_path']):
                    return False
                    
            # Save and proceed
            if not self.save_recipient_info():
                return False
                
            if not self.click_next_button():
                return False
                
            print("Recipient details only process completed successfully.")
            return True
            
        except Exception as e:
            print(f"Error in recipient details only process: {e}")
            return False
