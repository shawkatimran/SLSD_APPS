from pages.dashboard.TransferMutationPage import TransferMutationPage
from config import BASE_URL
import pytest

class TestTransferMutation:
    
    def test_transfer_mutation_first_step(self, driver):
        """Test the first step of transfer mutation process"""
        driver.get(BASE_URL)
        
        transfer_mutation_page = TransferMutationPage(driver)
        
        # Test data
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
        
        # Execute the test
        result = transfer_mutation_page.complete_first_step(
            institute_data=institute_data,
            property_data=property_data,
            construction_data=construction_data,
            basement_parking_data=basement_parking_data,
            document_paths=document_paths
        )
        
        assert result, "Transfer mutation first step should complete successfully"
        
    def test_transfer_mutation_basic_flow(self, driver):
        """Test basic transfer mutation flow without optional data"""
        driver.get(BASE_URL)
        
        transfer_mutation_page = TransferMutationPage(driver)
        
        # Test navigation and basic selections only
        assert transfer_mutation_page.click_dropdown_menu()
        assert transfer_mutation_page.click_transfer_mutation_option()
        assert transfer_mutation_page.click_new_application()
        assert transfer_mutation_page.select_source_of_transfer_buy()
        assert transfer_mutation_page.select_plot_flat_type_residential()
        
    def test_individual_form_sections(self, driver):
        """Test individual form sections separately"""
        driver.get(BASE_URL)
        
        transfer_mutation_page = TransferMutationPage(driver)
        
        # Setup initial navigation
        transfer_mutation_page.click_dropdown_menu()
        transfer_mutation_page.click_transfer_mutation_option()
        transfer_mutation_page.click_new_application()
        transfer_mutation_page.select_source_of_transfer_buy()
        transfer_mutation_page.select_plot_flat_type_residential()
        
        # Test mortgage options
        assert transfer_mutation_page.select_mortgage_options()
        
        # Test property details
        property_data = {
            "street_no": "32",
            "transferable_land_qty": "0.04", 
            "memorial_no": "25.00.0010.090.019.23.0945.25"
        }
        assert transfer_mutation_page.fill_property_details(**property_data)
        
        # Test construction details
        construction_data = {
            "floor_count": 14,
            "flat_size": 1450
        }
        assert transfer_mutation_page.fill_construction_details(**construction_data)
