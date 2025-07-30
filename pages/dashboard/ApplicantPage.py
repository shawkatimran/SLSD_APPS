from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from pages.BasePage import BasePage
import time

class ApplicantPage(BasePage):
    # Locators for Select Applicant
    APPLICANT_ROW = (By.XPATH, "//td[contains(text(),'মুহাঃ জয়নাল আবেদীন')]/parent::tr")
    SELECT_BUTTON = (By.XPATH, ".//button[contains(@onclick, 'getAssetOwner')]")
    
    # Locators for Applicant Details
    APPLICANT_MOBILE = (By.ID, 'applicant_mobile')
    APPLICANT_EMAIL = (By.ID, 'applicant_email')
    APPLICANT_TIN = (By.ID, 'applicant_tin_no')
    APPLICANT_TRANSFERABLE_LAND_QTY = (By.ID, 'applicant_transferable_land_qty')
    
    # Dropdown locators
    DISTRICT_DROPDOWN = (By.ID, "applicant_present_district_id")
    THANA_DROPDOWN = (By.ID, "applicant_present_thana_id")
    
    # Address checkbox
    SAME_ADDRESS_CHECKBOX = (By.XPATH, "//label[@for='applicant_is_pp_same_address' and contains(text(), 'স্থায়ী ও বর্তমান ঠিকানা একই')]")
    
    # File upload locators
    SIGNATURE_INPUT = (By.ID, 'applicant_signature')
    PHOTO_INPUT = (By.ID, 'applicant_photo')
    CROP_IMAGE_BUTTON = (By.ID, 'cropImageBtn')
    
    # Save buttons
    DONOR_INFO_SAVE_BUTTON = (By.ID, 'applicant_saveInfo')
    NEXT_BUTTON = (By.XPATH, '//a[@class="next" and @href="#next"]')

    def wait_for_applicant_table(self):
        """Wait for the applicant table to load"""
        try:
            self.wait.until(EC.presence_of_element_located((By.XPATH, "//td[contains(text(),'মুহাঃ জয়নাল আবেদীন')]")))
            print("Applicant table loaded successfully.")
            return True
        except TimeoutException as e:
            print(f"Failed to load applicant table: {e}")
            return False

    def get_applicant_info(self):
        """Get applicant information from the table row"""
        try:
            row = self.driver.find_element(*self.APPLICANT_ROW)
            columns = row.find_elements(By.TAG_NAME, "td")
            
            name = columns[0].text.strip()
            phone = columns[1].text.strip()
            
            print(f"Name: {name}")
            print(f"Phone: {phone}")
            
            return {"name": name, "phone": phone}
        except Exception as e:
            print(f"Failed to get applicant info: {e}")
            return None

    def select_applicant(self):
        """Select the applicant from the table"""
        try:
            if not self.wait_for_applicant_table():
                return False
                
            # Get applicant info for verification
            applicant_info = self.get_applicant_info()
            if not applicant_info:
                return False
                
            # Click the select button
            row = self.driver.find_element(*self.APPLICANT_ROW)
            select_button = row.find_element(*self.SELECT_BUTTON)
            select_button.click()
            print("Applicant selected successfully.")
            return True
            
        except (TimeoutException, ElementNotInteractableException) as e:
            print(f"Failed to select applicant: {e}")
            return False

    def fill_applicant_contact_info(self, mobile, email, tin):
        """Fill applicant contact information"""
        try:
            # Fill mobile number
            self.send_keys(self.APPLICANT_MOBILE, mobile)
            print(f"Entered mobile number: {mobile}")
            
            # Fill email
            self.send_keys(self.APPLICANT_EMAIL, email)
            print(f"Entered email: {email}")
            
            # Fill TIN number
            self.send_keys(self.APPLICANT_TIN, tin)
            print(f"Entered TIN number: {tin}")
            
            return True
        except Exception as e:
            print(f"Failed to fill contact info: {e}")
            return False

    def fill_land_quantity(self, quantity):
        """Fill transferable land quantity"""
        try:
            self.send_keys(self.APPLICANT_TRANSFERABLE_LAND_QTY, quantity)
            print(f"Entered transferable land quantity: {quantity}")
            return True
        except Exception as e:
            print(f"Failed to fill land quantity: {e}")
            return False

    def select_district_and_thana(self, district, thana):
        """Select district and thana from dropdowns"""
        try:
            # Select district
            district_dropdown = self.driver.find_element(*self.DISTRICT_DROPDOWN)
            district_select = Select(district_dropdown)
            district_select.select_by_visible_text(district)
            print(f"Selected district: {district}")
            time.sleep(3)
            
            # Select thana
            thana_dropdown = self.driver.find_element(*self.THANA_DROPDOWN)
            thana_select = Select(thana_dropdown)
            thana_select.select_by_visible_text(thana)
            print(f"Selected thana: {thana}")
            
            return True
        except Exception as e:
            print(f"Failed to select district/thana: {e}")
            return False

    def click_same_address_checkbox(self):
        """Click the same address checkbox"""
        try:
            checkbox = self.driver.find_element(*self.SAME_ADDRESS_CHECKBOX)
            time.sleep(2)
            checkbox.click()
            print("Clicked same address checkbox.")
            time.sleep(3)
            return True
        except Exception as e:
            print(f"Failed to click same address checkbox: {e}")
            return False

    def upload_signature(self, signature_path):
        """Upload applicant signature"""
        try:
            # Upload signature file
            signature_input = self.driver.find_element(*self.SIGNATURE_INPUT)
            signature_input.send_keys(signature_path)
            print(f"Signature uploaded: {signature_path}")
            
            # Click save button
            save_button = self.wait.until(EC.element_to_be_clickable(self.CROP_IMAGE_BUTTON))
            save_button.click()
            print("Signature saved.")
            time.sleep(2)
            
            return True
        except Exception as e:
            print(f"Failed to upload signature: {e}")
            return False

    def upload_photo(self, photo_path):
        """Upload applicant photo"""
        try:
            # Upload photo file
            photo_input = self.driver.find_element(*self.PHOTO_INPUT)
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
            print(f"Failed to upload photo: {e}")
            return False

    def save_donor_info(self):
        """Save donor information"""
        try:
            save_button = self.wait.until(EC.element_to_be_clickable(self.DONOR_INFO_SAVE_BUTTON))
            save_button.click()
            print("Donor information saved.")
            time.sleep(10)
            return True
        except Exception as e:
            print(f"Failed to save donor info: {e}")
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

    def complete_applicant_selection_and_details(self, contact_info=None, location_info=None, 
                                                file_paths=None, land_quantity="0.04"):
        """Complete the entire applicant selection and details process"""
        try:
            # Step 1: Select applicant
            if not self.select_applicant():
                return False
                
            # Step 2: Fill contact information
            if contact_info:
                if not self.fill_applicant_contact_info(**contact_info):
                    return False
            
            # Step 3: Fill land quantity
            if not self.fill_land_quantity(land_quantity):
                return False
                
            # Step 4: Select location
            if location_info:
                if not self.select_district_and_thana(**location_info):
                    return False
                    
            # Step 5: Click same address checkbox
            if not self.click_same_address_checkbox():
                return False
                
            # Step 6: Upload files
            if file_paths:
                if 'signature_path' in file_paths:
                    if not self.upload_signature(file_paths['signature_path']):
                        return False
                        
                if 'photo_path' in file_paths:
                    if not self.upload_photo(file_paths['photo_path']):
                        return False
                        
            # Step 7: Save donor info
            if not self.save_donor_info():
                return False
                
            # Step 8: Click next
            if not self.click_next_button():
                return False
                
            print("Applicant selection and details completed successfully.")
            return True
            
        except Exception as e:
            print(f"Error completing applicant process: {e}")
            return False

    def fill_applicant_details_only(self, contact_info, location_info, file_paths, land_quantity="0.04"):
        """Fill applicant details without selection (for when applicant is already selected)"""
        try:
            # Fill contact information
            if not self.fill_applicant_contact_info(**contact_info):
                return False
            
            # Fill land quantity
            if not self.fill_land_quantity(land_quantity):
                return False
                
            # Select location
            if not self.select_district_and_thana(**location_info):
                return False
                
            # Click same address checkbox
            if not self.click_same_address_checkbox():
                return False
                
            # Upload files
            if 'signature_path' in file_paths:
                if not self.upload_signature(file_paths['signature_path']):
                    return False
                    
            if 'photo_path' in file_paths:
                if not self.upload_photo(file_paths['photo_path']):
                    return False
                    
            # Save donor info
            if not self.save_donor_info():
                return False
                
            # Click next
            if not self.click_next_button():
                return False
                
            print("Applicant details filled successfully.")
            return True
            
        except Exception as e:
            print(f"Error filling applicant details: {e}")
            return False
