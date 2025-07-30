from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from pages.BasePage import BasePage
import time

class TransferMutationPage(BasePage):
    # Locators
    DROPDOWN_MENU = (By.XPATH, '//a[@class="dash-menu-text" and @data-toggle="collapse"]')
    DROPDOWN_ITEM = (By.XPATH, '//a[contains(@href, "plot-flat-transfer/list") and contains(text(), "প্লট/ফ্ল্যাট হস্তান্তর ও নামজারি")]')
    NEW_APPLICATION_BUTTON = (By.XPATH, '//button[contains(text(), "নতুন আবেদন")]')
    
    # Source of Transfer - Radio button and its label
    SOURCE_OF_TRANSFER_BUY_RADIO = (By.ID, "transfer_rules_1")
    SOURCE_OF_TRANSFER_BUY_LABEL = (By.XPATH, '//label[@for="transfer_rules_1"]')
    SOURCE_OF_TRANSFER_BUY = (By.XPATH, '//label[@for="transfer_rules_1" and contains(text(), "ক্রয়")]')
    SOURCE_OF_TRANSFER_BUY_ALT1 = (By.XPATH, "//label[contains(text(), 'ক্রয়')]")
    SOURCE_OF_TRANSFER_BUY_ALT2 = (By.XPATH, "//input[@id='transfer_rules_1']/../label")
    SOURCE_OF_TRANSFER_BUY_ALT3 = (By.ID, "transfer_rules_1")

    
    
    # Plot/Flat Type
    PLOT_FLAT_TYPE_RESIDENTIAL = (By.XPATH, '//label[@for="customer_rules_1" and contains(text(), "আবাসিক")]')
    
    # Institute Information
    INSTITUTE_NAME_BANGLA = (By.ID, 'person_institute_name_bangla')
    INSTITUTE_NAME_ENGLISH = (By.ID, 'person_institute_name_english')
    MOBILE_NUMBER = (By.ID, 'business_mobile_number')
    EMAIL_ADDRESS = (By.ID, 'email_address')
    INSTITUTE_ADDRESS = (By.ID, 'institute_address')
    
    # Mortgage Options - Radio buttons/checkboxes and their labels
    MORTGAGE_YES_RADIO = (By.ID, "mortgageYes")
    MORTGAGE_YES_LABEL = (By.XPATH, '//label[@for="mortgageYes"]')
    MORTGAGE_YES = (By.XPATH, '//label[@for="mortgageYes"]')
    
    MORTGAGE_DEED_YES_RADIO = (By.ID, "mortgageDeedYes")
    MORTGAGE_DEED_YES_LABEL = (By.XPATH, '//label[@for="mortgageDeedYes"]')
    MORTGAGE_DEED_YES = (By.XPATH, '//label[@for="mortgageDeedYes"]')
    
    # File Uploads
    LOAN_WAIVER_DEED = (By.ID, 'loan_waiver_deed')
    LOAN_PAYMENT_NOC_FILE = (By.ID, 'loan_payment_noc_file')
    
    # Property Details
    STREET_NO = (By.ID, 'street_no')
    TRANSFERABLE_LAND_QTY = (By.ID, 'transferable_land_qty')
    
    # Construction Details
    STRUCTURE_YES = (By.XPATH, '//label[@for="structureYes"]')
    MEMORIAL_NO = (By.ID, 'memorial_no')
    DESIGN_YES = (By.XPATH, '//label[@for="designYes"]')
    HOW_MANY_FLOOR = (By.ID, 'how_many_floor')
    SAME_SIZE_YES = (By.XPATH, '//label[@for="sameSizeYes"]')
    SIZE_OF_EACH_FLAT = (By.ID, 'size_of_each_flat')
    
    # Basement and Parking
    BASEMENT_YES = (By.XPATH, '//label[@for="basementYes"]')
    BASEMENT_NO = (By.ID, 'basement_no')
    PARKING_YES = (By.XPATH, '//label[@for="parkingYes"]')
    PARKING_NO = (By.ID, 'parking_no')
    
    # Navigation
    NEXT_BUTTON = (By.XPATH, '//a[@class="next" and @href="#next"]')

    def click_dropdown_menu(self):
        """Click the dropdown menu to access plot/flat transfer options"""
        try:
            self.click(self.DROPDOWN_MENU)
            print("Dropdown menu clicked.")
            return True
        except (TimeoutException, ElementNotInteractableException) as e:
            print(f"Failed to click dropdown menu: {e}")
            return False

    def click_transfer_mutation_option(self):
        """Click on the plot/flat transfer option in dropdown"""
        try:
            dropdown_item = self.wait.until(EC.element_to_be_clickable(self.DROPDOWN_ITEM))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", dropdown_item)
            dropdown_item.click()
            print("Dropdown item clicked.")
            return True
        except (TimeoutException, ElementNotInteractableException) as e:
            print(f"Failed to click dropdown item: {e}")
            return False

    def click_new_application(self):
        """Click the new application button"""
        try:
            self.click(self.NEW_APPLICATION_BUTTON)
            print("New application button clicked.")
            return True
        except (TimeoutException, ElementNotInteractableException) as e:
            print(f"Failed to click new application button: {e}")
            return False

    def select_source_of_transfer_buy(self):
        """Select 'ক্রয়' radio button as source of transfer"""
        try:
            print("Attempting to select 'ক্রয়' radio button...")
            
            # Strategy 1: Click the radio button input directly
            try:
                print("Strategy 1: Clicking radio button input directly")
                radio_input = self.wait.until(EC.presence_of_element_located(self.SOURCE_OF_TRANSFER_BUY_RADIO))
                
                # Scroll to radio button
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", radio_input)
                time.sleep(1)
                
                # Check if already selected
                if radio_input.is_selected():
                    print("Radio button is already selected.")
                    return True
                
                # Try clicking the radio button directly
                try:
                    radio_input.click()
                    print("Radio button clicked directly.")
                    return True
                except:
                    # Try JavaScript click on radio button
                    self.driver.execute_script("arguments[0].click();", radio_input)
                    print("Radio button clicked with JavaScript.")
                    return True
                    
            except Exception as e:
                print(f"Strategy 1 failed: {e}")
            
            # Strategy 2: Click the label associated with the radio button
            try:
                print("Strategy 2: Clicking the label for the radio button")
                label = self.wait.until(EC.element_to_be_clickable(self.SOURCE_OF_TRANSFER_BUY_LABEL))
                
                # Scroll to label
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", label)
                time.sleep(1)
                
                # Try normal click on label
                try:
                    label.click()
                    print("Label clicked successfully.")
                    return True
                except:
                    # Try JavaScript click on label
                    self.driver.execute_script("arguments[0].click();", label)
                    print("Label clicked with JavaScript.")
                    return True
                    
            except Exception as e:
                print(f"Strategy 2 failed: {e}")
            
            # Strategy 3: Use JavaScript to set radio button value
            try:
                print("Strategy 3: Using JavaScript to set radio button")
                # Find the radio button and set it programmatically
                self.driver.execute_script("""
                    var radioButton = document.getElementById('transfer_rules_1');
                    if (radioButton) {
                        radioButton.checked = true;
                        radioButton.dispatchEvent(new Event('change', { bubbles: true }));
                        radioButton.dispatchEvent(new Event('click', { bubbles: true }));
                    }
                """)
                print("Radio button set with JavaScript.")
                time.sleep(1)
                
                # Verify if it's selected
                radio_input = self.driver.find_element(*self.SOURCE_OF_TRANSFER_BUY_RADIO)
                if radio_input.is_selected():
                    print("Radio button successfully selected.")
                    return True
                    
            except Exception as e:
                print(f"Strategy 3 failed: {e}")
            
            # Strategy 4: Try clicking the text content directly
            try:
                print("Strategy 4: Clicking by text content")
                text_element = self.driver.find_element(By.XPATH, "//label[contains(text(), 'ক্রয়')]")
                
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", text_element)
                time.sleep(1)
                
                # Try clicking the text element
                try:
                    text_element.click()
                    print("Text element clicked successfully.")
                    return True
                except:
                    self.driver.execute_script("arguments[0].click();", text_element)
                    print("Text element clicked with JavaScript.")
                    return True
                    
            except Exception as e:
                print(f"Strategy 4 failed: {e}")
            
            # Strategy 5: Find parent container and click
            try:
                print("Strategy 5: Clicking parent container")
                parent_element = self.driver.find_element(By.XPATH, "//input[@id='transfer_rules_1']/parent::*")
                
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", parent_element)
                time.sleep(1)
                self.driver.execute_script("arguments[0].click();", parent_element)
                print("Parent container clicked.")
                return True
                
            except Exception as e:
                print(f"Strategy 5 failed: {e}")
            
            print("All strategies failed to select the radio button!")
            return False
            
        except Exception as e:
            print(f"Critical error in select_source_of_transfer_buy: {e}")
            return False

    def select_plot_flat_type_residential(self):
        """Select 'আবাসিক' as plot/flat type"""
        try:
            self.click(self.PLOT_FLAT_TYPE_RESIDENTIAL)
            print("Plot/Flat Type (Residential) selected.")
            return True
        except (TimeoutException, ElementNotInteractableException) as e:
            print(f"Failed to select plot/flat type: {e}")
            return False

    def fill_institute_information(self, name_bangla, name_english, mobile, email, address):
        """Fill institute information fields"""
        try:
            self.send_keys(self.INSTITUTE_NAME_BANGLA, name_bangla)
            print("Institute name (Bangla) entered.")
            
            self.send_keys(self.INSTITUTE_NAME_ENGLISH, name_english)
            print("Institute name (English) entered.")
            
            self.send_keys(self.MOBILE_NUMBER, mobile)
            print("Mobile number entered.")
            
            self.send_keys(self.EMAIL_ADDRESS, email)
            print("Email address entered.")
            
            self.send_keys(self.INSTITUTE_ADDRESS, address)
            print("Institute address entered.")
            return True
        except (TimeoutException, ElementNotInteractableException) as e:
            print(f"Failed to fill institute information: {e}")
            return False

    def select_mortgage_yes(self):
        """Select 'Yes' for mortgage permission with enhanced strategies"""
        try:
            print("Attempting to select 'Yes' for mortgage permission...")
            
            # Strategy 1: Direct radio button selection with multiple attempts
            try:
                print("Strategy 1: Clicking mortgage radio button directly")
                input_element = self.wait.until(EC.presence_of_element_located(self.MORTGAGE_YES_RADIO))
                
                # Scroll to element and make it visible
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", input_element)
                time.sleep(1)
                
                # Make sure element is visible and enabled
                self.driver.execute_script("arguments[0].style.display = 'block'; arguments[0].style.visibility = 'visible';", input_element)
                time.sleep(1)
                
                # Check if already selected
                if input_element.is_selected():
                    print("Mortgage radio button is already selected.")
                    return True
                
                # Try clicking directly first
                try:
                    # Wait for clickable
                    clickable_element = self.wait.until(EC.element_to_be_clickable(self.MORTGAGE_YES_RADIO))
                    clickable_element.click()
                    print("Mortgage radio button clicked directly.")
                    time.sleep(1)
                    
                    # Verify selection
                    if clickable_element.is_selected():
                        print("Mortgage radio button successfully selected.")
                        return True
                        
                except Exception as click_e:
                    print(f"Direct click failed: {click_e}")
                    
                # Try JavaScript click
                try:
                    self.driver.execute_script("arguments[0].click();", input_element)
                    print("Mortgage radio button clicked with JavaScript.")
                    time.sleep(1)
                    
                    # Verify selection
                    if input_element.is_selected():
                        print("Mortgage radio button successfully selected with JS.")
                        return True
                        
                except Exception as js_e:
                    print(f"JavaScript click failed: {js_e}")
                    
            except Exception as e:
                print(f"Strategy 1 failed: {e}")
            
            # Strategy 2: Click the associated label
            try:
                print("Strategy 2: Clicking the mortgage label")
                label = self.wait.until(EC.presence_of_element_located(self.MORTGAGE_YES_LABEL))
                
                # Scroll to label
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", label)
                time.sleep(1)
                
                # Try normal click on label
                try:
                    label.click()
                    print("Mortgage label clicked successfully.")
                    time.sleep(1)
                    
                    # Check if radio button is now selected
                    radio_input = self.driver.find_element(*self.MORTGAGE_YES_RADIO)
                    if radio_input.is_selected():
                        print("Radio button selected via label click.")
                        return True
                        
                except Exception as label_click_e:
                    print(f"Label click failed: {label_click_e}")
                    
                # Try JavaScript click on label
                try:
                    self.driver.execute_script("arguments[0].click();", label)
                    print("Mortgage label clicked with JavaScript.")
                    time.sleep(1)
                    
                    # Check if radio button is now selected
                    radio_input = self.driver.find_element(*self.MORTGAGE_YES_RADIO)
                    if radio_input.is_selected():
                        print("Radio button selected via JS label click.")
                        return True
                        
                except Exception as js_label_e:
                    print(f"JS label click failed: {js_label_e}")
                    
            except Exception as e:
                print(f"Strategy 2 failed: {e}")
            
            # Strategy 3: JavaScript programmatic selection
            try:
                print("Strategy 3: Using JavaScript to programmatically set mortgage option")
                self.driver.execute_script("""
                    var element = document.getElementById('mortgageYes');
                    if (element) {
                        element.checked = true;
                        element.click();
                        
                        // Trigger events
                        var changeEvent = new Event('change', { bubbles: true });
                        var clickEvent = new Event('click', { bubbles: true });
                        element.dispatchEvent(changeEvent);
                        element.dispatchEvent(clickEvent);
                        
                        // Also try triggering input event
                        var inputEvent = new Event('input', { bubbles: true });
                        element.dispatchEvent(inputEvent);
                    }
                """)
                print("Mortgage option set with JavaScript programmatically.")
                time.sleep(2)
                
                # Verify selection
                try:
                    radio_input = self.driver.find_element(*self.MORTGAGE_YES_RADIO)
                    if radio_input.is_selected():
                        print("Radio button successfully selected programmatically.")
                        return True
                except:
                    pass
                    
            except Exception as e:
                print(f"Strategy 3 failed: {e}")
            
            # Strategy 4: Find by text and click
            try:
                print("Strategy 4: Finding mortgage option by text content")
                # Look for text that might be associated with mortgage yes option
                text_elements = self.driver.find_elements(By.XPATH, "//label[contains(text(), 'হ্যাঁ') or contains(text(), 'Yes')]")
                
                for element in text_elements:
                    try:
                        # Check if this label is for mortgageYes
                        for_attr = element.get_attribute('for')
                        if for_attr == 'mortgageYes':
                            self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
                            time.sleep(1)
                            self.driver.execute_script("arguments[0].click();", element)
                            print("Found mortgage yes label by text and clicked.")
                            time.sleep(1)
                            
                            # Verify
                            radio_input = self.driver.find_element(*self.MORTGAGE_YES_RADIO)
                            if radio_input.is_selected():
                                print("Radio button selected via text search.")
                                return True
                    except:
                        continue
                        
            except Exception as e:
                print(f"Strategy 4 failed: {e}")
            
            # Strategy 5: Force selection with form manipulation
            try:
                print("Strategy 5: Force selection with form manipulation")
                self.driver.execute_script("""
                    // Find the mortgage radio button
                    var mortgageRadio = document.getElementById('mortgageYes');
                    if (mortgageRadio) {
                        // Force visibility and enable
                        mortgageRadio.style.display = 'block';
                        mortgageRadio.style.visibility = 'visible';
                        mortgageRadio.disabled = false;
                        mortgageRadio.readonly = false;
                        
                        // Set checked state
                        mortgageRadio.checked = true;
                        mortgageRadio.value = 'yes';
                        
                        // Trigger all possible events
                        ['click', 'change', 'input', 'focus', 'blur'].forEach(function(eventType) {
                            var event = new Event(eventType, { bubbles: true, cancelable: true });
                            mortgageRadio.dispatchEvent(event);
                        });
                        
                        // Also trigger jQuery events if available
                        if (typeof jQuery !== 'undefined') {
                            jQuery(mortgageRadio).trigger('click').trigger('change');
                        }
                    }
                """)
                print("Force selection attempted.")
                time.sleep(2)
                
                # Final verification
                try:
                    radio_input = self.driver.find_element(*self.MORTGAGE_YES_RADIO)
                    if radio_input.is_selected():
                        print("Radio button successfully force-selected.")
                        return True
                except:
                    pass
                    
            except Exception as e:
                print(f"Strategy 5 failed: {e}")
            
            print("All strategies failed for mortgage selection!")
            return False
            
        except Exception as e:
            print(f"Critical error in select_mortgage_yes: {e}")
            return False

    def select_mortgage_deed_yes(self):
        """Select 'Yes' for mortgage deed"""
        try:
            print("Attempting to select 'Yes' for mortgage deed...")
            
            # Strategy 1: Click the radio button/checkbox input directly
            try:
                print("Strategy 1: Clicking mortgage deed input directly")
                input_element = self.wait.until(EC.presence_of_element_located(self.MORTGAGE_DEED_YES_RADIO))
                
                # Scroll to element
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", input_element)
                time.sleep(1)
                
                # Check if already selected
                if input_element.is_selected():
                    print("Mortgage deed option is already selected.")
                    return True
                
                # Try clicking directly
                try:
                    input_element.click()
                    print("Mortgage deed input clicked directly.")
                    return True
                except:
                    # Try JavaScript click
                    self.driver.execute_script("arguments[0].click();", input_element)
                    print("Mortgage deed input clicked with JavaScript.")
                    return True
                    
            except Exception as e:
                print(f"Strategy 1 failed: {e}")
            
            # Strategy 2: Click the label
            try:
                print("Strategy 2: Clicking the mortgage deed label")
                label = self.wait.until(EC.element_to_be_clickable(self.MORTGAGE_DEED_YES_LABEL))
                
                # Scroll to label
                self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", label)
                time.sleep(1)
                
                try:
                    label.click()
                    print("Mortgage deed label clicked successfully.")
                    return True
                except:
                    self.driver.execute_script("arguments[0].click();", label)
                    print("Mortgage deed label clicked with JavaScript.")
                    return True
                    
            except Exception as e:
                print(f"Strategy 2 failed: {e}")
            
            # Strategy 3: JavaScript selection
            try:
                print("Strategy 3: Using JavaScript to set mortgage deed option")
                self.driver.execute_script("""
                    var element = document.getElementById('mortgageDeedYes');
                    if (element) {
                        element.checked = true;
                        element.dispatchEvent(new Event('change', { bubbles: true }));
                        element.dispatchEvent(new Event('click', { bubbles: true }));
                    }
                """)
                print("Mortgage deed option set with JavaScript.")
                return True
                
            except Exception as e:
                print(f"Strategy 3 failed: {e}")
            
            print("All strategies failed for mortgage deed selection!")
            return False
            
        except Exception as e:
            print(f"Critical error in select_mortgage_deed_yes: {e}")
            return False

    def select_mortgage_options(self):
        """Select mortgage related options"""
        try:
            # Select mortgage permission yes
            if not self.select_mortgage_yes():
                print("Failed to select mortgage permission option.")
                return False
            
            # Select mortgage deed yes
            if not self.select_mortgage_deed_yes():
                print("Failed to select mortgage deed option.")
                return False
                
            print("All mortgage options selected successfully.")
            return True
            
        except Exception as e:
            print(f"Failed to select mortgage options: {e}")
            return False

    def upload_documents(self, loan_waiver_deed_path, loan_payment_noc_path):
        """Upload required documents"""
        try:
            # Upload loan waiver deed
            lwd_element = self.wait.until(EC.element_to_be_clickable(self.LOAN_WAIVER_DEED))
            lwd_element.send_keys(loan_waiver_deed_path)
            print(f"Loan waiver deed uploaded: {loan_waiver_deed_path}")
            time.sleep(5)
            
            # Upload loan payment NOC
            noc_element = self.wait.until(EC.element_to_be_clickable(self.LOAN_PAYMENT_NOC_FILE))
            noc_element.send_keys(loan_payment_noc_path)
            print(f"Loan payment NOC uploaded: {loan_payment_noc_path}")
            time.sleep(5)
            return True
        except (TimeoutException, ElementNotInteractableException) as e:
            print(f"Failed to upload documents: {e}")
            return False

    def fill_property_details(self, street_no, transferable_land_qty, memorial_no):
        """Fill property details"""
        try:
            self.send_keys(self.STREET_NO, street_no)
            print(f"Street number entered: {street_no}")
            
            self.send_keys(self.TRANSFERABLE_LAND_QTY, transferable_land_qty)
            print(f"Transferable land quantity entered: {transferable_land_qty}")
            
            self.send_keys(self.MEMORIAL_NO, memorial_no)
            print(f"Memorial number entered: {memorial_no}")
            return True
        except (TimeoutException, ElementNotInteractableException) as e:
            print(f"Failed to fill property details: {e}")
            return False

    def fill_construction_details(self, floor_count, flat_size):
        """Fill construction and building details"""
        try:
            # Select structure yes
            self.click(self.STRUCTURE_YES)
            print("Structure 'Yes' selected.")
            
            # Select design approval yes
            self.click(self.DESIGN_YES)
            print("Design approval 'Yes' selected.")
            
            # Enter floor count
            self.send_keys(self.HOW_MANY_FLOOR, str(floor_count))
            print(f"Floor count entered: {floor_count}")
            
            # Select same size yes
            self.click(self.SAME_SIZE_YES)
            print("Same flat size 'Yes' selected.")
            
            # Enter flat size
            self.send_keys(self.SIZE_OF_EACH_FLAT, str(flat_size))
            print(f"Flat size entered: {flat_size}")
            return True
        except (TimeoutException, ElementNotInteractableException) as e:
            print(f"Failed to fill construction details: {e}")
            return False

    def fill_basement_and_parking(self, basement_count, parking_count):
        """Fill basement and parking information"""
        try:
            # Select basement yes
            basement_element = self.wait.until(EC.element_to_be_clickable(self.BASEMENT_YES))
            basement_element.click()
            print("Basement 'Yes' selected.")
            
            # Enter basement count
            basement_no_element = self.wait.until(EC.presence_of_element_located(self.BASEMENT_NO))
            self.driver.execute_script("arguments[0].scrollIntoView(true);", basement_no_element)
            basement_no_element.send_keys(str(basement_count))
            print(f"Basement count entered: {basement_count}")
            
            # Select parking yes
            self.click(self.PARKING_YES)
            print("Parking 'Yes' selected.")
            
            # Enter parking count
            self.send_keys(self.PARKING_NO, str(parking_count))
            print(f"Parking count entered: {parking_count}")
            return True
        except (TimeoutException, ElementNotInteractableException) as e:
            print(f"Failed to fill basement and parking details: {e}")
            return False

    def click_next_button(self):
        """Click the next button to proceed"""
        try:
            self.click(self.NEXT_BUTTON)
            print("Next button clicked.")
            return True
        except (TimeoutException, ElementNotInteractableException) as e:
            print(f"Failed to click next button: {e}")
            return False

    def complete_first_step(self, institute_data=None, property_data=None, construction_data=None, 
                          basement_parking_data=None, document_paths=None):
        """Complete the entire first step of transfer mutation process"""
        try:
            # Navigate to transfer mutation
            if not self.click_dropdown_menu():
                return False
            if not self.click_transfer_mutation_option():
                return False
            if not self.click_new_application():
                return False
                
            # Select basic options
            if not self.select_source_of_transfer_buy():
                return False
            if not self.select_plot_flat_type_residential():
                return False
                
            # Fill institute information if provided
            if institute_data:
                if not self.fill_institute_information(**institute_data):
                    return False
                    
            # Select mortgage options
            if not self.select_mortgage_options():
                return False
                
            # Upload documents if provided
            if document_paths:
                if not self.upload_documents(**document_paths):
                    return False
                    
            # Fill property details if provided
            if property_data:
                if not self.fill_property_details(**property_data):
                    return False
                    
            # Fill construction details if provided
            if construction_data:
                if not self.fill_construction_details(**construction_data):
                    return False
                    
            # Fill basement and parking if provided
            if basement_parking_data:
                if not self.fill_basement_and_parking(**basement_parking_data):
                    return False
                    
            # Click next to proceed
            if not self.click_next_button():
                return False
                
            print("First step completed successfully.")
            return True
            
        except Exception as e:
            print(f"Error completing first step: {e}")
            return False
