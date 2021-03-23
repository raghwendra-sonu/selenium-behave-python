import time
from objectRepo.locators import Home
from allocator.reusableLibrary import Reusable

class HomePage(Reusable):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = HomePage()
        return cls.instance

    def __init__(self):
        super().__init__()

    def create_an_account(self, account_name):
        time.sleep(3)
        super().perform_action_on_element(Home.new_account_tab, "Click")
        time.sleep(3)
        super().perform_action_on_element(Home.NewAccount, "ClickWithActionClass")
        super().perform_action_on_element(Home.account_name_txtbox_new_account_window, "Type", account_name)
        super().perform_action_on_element(Home.salesforce_save_btn_NewAccountWindow, "Click")
        time.sleep(3)

    def verify_account_created(self, account_name):
        super().get_dynamic_text_from_element(Home.salesforce_name_of_new_account, account_name)

    def delete_an_account(self, account_name):
        super().perform_action_on_element(Home.dynamic_text, "ClickWithActionClass", "Accounts")
        super().perform_action_on_element(Home.primitive_icon, "Click", account_name)
        super().perform_action_on_element(Home.delete, "Click", )
        super().perform_action_on_element(Home.delete_popup, "Click")

    def verify_navigation(self):
        super().perform_action_on_element(Home.dynamic_text, "ClickWithActionClass", "Accounts")
        super().perform_action_on_element(Home.dynamic_text, "ClickWithActionClass", "Patrons")
        super().perform_action_on_element(Home.dynamic_text, "ClickWithActionClass", "Prospects")
        super().perform_action_on_element(Home.dynamic_text, "ClickWithActionClass", "Opportunities")
        super().perform_action_on_element(Home.dynamic_text, "ClickWithActionClass", "Tasks")
        super().perform_action_on_element(Home.dynamic_text, "ClickWithActionClass", "Calendar")
        super().perform_action_on_element(Home.dynamic_text, "ClickWithActionClass", "Groups")
        super().perform_action_on_element(Home.dynamic_text, "ClickWithActionClass", "Notes")
        super().perform_action_on_element(Home.dynamic_text, "ClickWithActionClass", "Reports")
        super().perform_action_on_element(Home.dynamic_text, "ClickWithActionClass", "More")
        super().perform_action_on_element(Home.dynamic_text, "ClickWithActionClass", "Home")

    def select_user_role(self, role):
        super().perform_action_on_element(Home.AppLauncher, "Click")
        time.sleep(3)
        super().perform_action_on_element(Home.view_all_link, "Click")
        super().perform_action_on_element(Home.dynamic_text, "scroll", role)
        super().perform_action_on_element(Home.Role, "ClickWithActionClass", role)




home_page = HomePage.get_instance()