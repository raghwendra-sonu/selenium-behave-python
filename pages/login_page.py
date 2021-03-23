from objectRepo.locators import SignInPage, Home
from allocator.reusableLibrary import Reusable

class LoginPage(Reusable):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = LoginPage()
        return cls.instance

    def __init__(self):
        super().__init__()

    def verify_user_loggedin(self, username):
        assert super().element_exists(Home.AppLauncher), username + " could not login to CRM application"

    def login(self, username, password):
        super().perform_action_on_element(SignInPage.UserName, "Type", username)
        super().perform_action_on_element(SignInPage.Password, "Type", password)
        super().perform_action_on_element(SignInPage.Login, "Click")
        super().element_exists(Home.AppLauncher)
        if (super().count_all_elements(SignInPage.login_popup)) != 0:
            super().perform_action_on_element(SignInPage.login_popup, "Click")
            self.driver.refresh();


login_page = LoginPage.get_instance()
