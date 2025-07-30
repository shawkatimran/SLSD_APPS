from pages.auth.LoginPage import LoginPage
from pages.dashboard.TransferMutationPage import TransferMutationPage
from pages.dashboard.ApplicantPage import ApplicantPage
from pages.dashboard.RecipientPage import RecipientPage
from pages.dashboard.AttachmentPage import AttachmentPage
from pages.dashboard.SubmitPage import SubmitPage
from config import LOGIN_PAGE_URL
from drivers import get_chrome_driver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, ElementNotInteractableException
from config import BASE_URL
from tests.auth.test_login import test_valid_login



def test_transfer_mutation(driver):
    
    try:
        test_valid_login(driver)
        
        # Initialize Transfer Mutation Page
        transfer_mutation_page = TransferMutationPage(driver)
        
        # Test data for first step
        institute_data = {
            "name_bangla": "বিজনেস অটোমেশন লিমিটেড",
            "name_english": "Business Automation Ltd",
            "mobile": "01563000030",
            "email": "test.email@gmail.com",
            "address": "BDBL Tower, 9th Floor, Karwane Bazar, Dhaka"
        }
        
        property_data = {
            "street_no": "32",
            "transferable_land_qty": "0.04",
            "memorial_no": "25.00.0010.090.019.23.0945.25"
        }
        
        construction_data = {
            "floor_count": 14,
            "flat_size": 1450
        }
        
        basement_parking_data = {
            "basement_count": 3,
            "parking_count": 2
        }
        
        document_paths = {
            "loan_waiver_deed_path": r"E:\AUTOMATION_TESTING\SLSD_APPLICATIONS\TEST_DATA\ঋণ_অবমুক্তি_দলিল .pdf",
            "loan_payment_noc_path": r"E:\AUTOMATION_TESTING\SLSD_APPLICATIONS\TEST_DATA\ঋণ_পরিশোধের_অনাপত্তিপত্র.pdf"
        }
        
        # Execute first step using Page Object Model
        first_step_result = transfer_mutation_page.complete_first_step(
            institute_data=institute_data,
            property_data=property_data,
            construction_data=construction_data,
            basement_parking_data=basement_parking_data,
            document_paths=document_paths
        )
        
        if not first_step_result:
            print("First step failed!")
            return

        # Initialize Applicant Page
        applicant_page = ApplicantPage(driver)
        
        # Test data for applicant step
        contact_info = {
            "mobile": "01777288811",
            "email": "bat@ba-systems.com", 
            "tin": "987654321101"
        }
        
        location_info = {
            "district": "যশোর",
            "thana": "যশোর সদর"
        }
        
        file_paths = {
            "signature_path": r"E:\AUTOMATION_TESTING\SLSD_APPLICATIONS\TEST_DATA\Photo\nazmul_huda.png",
            "photo_path": r"E:\AUTOMATION_TESTING\SLSD_APPLICATIONS\TEST_DATA\Photo\image_person.png"
        }
        
        # Execute applicant selection and details using Page Object Model
        applicant_result = applicant_page.complete_applicant_selection_and_details(
            contact_info=contact_info,
            location_info=location_info,
            file_paths=file_paths,
            land_quantity="0.04"
        )
        
        if not applicant_result:
            print("Applicant step failed!")
            return
        
        # Add a longer wait here for the page to transition
        time.sleep(5)
        
        # Initialize Recipient Page
        recipient_page = RecipientPage(driver)
        
        # Test data for recipient step
        brn_data = {
            "brn_number": "19827927501106437",
            "dob": "10-Aug-2016"
        }
        
        basic_info = {
            "name_bn": "জাহিদ হাসান আকাশ",
            "name_en": "Jahid Hassan Akash",
            "father_name": "শামসুর রহমান",
            "mother_name": "আয়শা মিতু",
            "spouse_name": "তানজিলা হক",
            "nationality": "Bangladeshi"
        }
        
        contact_info = {
            "mobile": "01777288812",
            "email": "prodhan@ba-systems.com",
            "tin": "987654329078"
        }
        
        location_info = {
            "district": "যশোর",
            "thana": "মনিরামপুর"
        }
        
        file_paths = {
            "signature_path": r"E:\AUTOMATION_TESTING\SLSD_APPLICATIONS\TEST_DATA\Photo\signature.jpeg",
            "photo_path": r"E:\AUTOMATION_TESTING\SLSD_APPLICATIONS\TEST_DATA\Photo\photo_2.jpg"
        }
        
        # Execute recipient process using Page Object Model
        recipient_result = recipient_page.complete_recipient_process(
            brn_data=brn_data,
            basic_info=basic_info,
            contact_info=contact_info,
            location_info=location_info,
            file_paths=file_paths
        )
        
        if not recipient_result:
            print("Recipient step failed!")
            return

        # Initialize Attachment Page
        attachment_page = AttachmentPage(driver)
        
        # Upload attachments using Page Object Model
        attachment_file_path = r"E:\AUTOMATION_TESTING\SLSD_APPLICATIONS\TEST_DATA\Test_Doc.pdf"
        attachment_result = attachment_page.upload_attachments(attachment_file_path)
        
        if not attachment_result:
            print("Attachment upload failed!")
            return

        # Initialize Submit Page
        submit_page = SubmitPage(driver)
        
        # Submit the form using Page Object Model
        submit_result = submit_page.submit_with_verification()
        
        if not submit_result:
            print("Form submission failed!")
            return
            
        print("Transfer mutation process completed successfully!")

    finally:

        driver.quit()
 
    

    


   

    
    




