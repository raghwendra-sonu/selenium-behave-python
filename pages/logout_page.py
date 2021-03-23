import time
from objectRepo.locators import Logout, SignInPage
from allocator.reusableLibrary import Reusable

class LogoutPage(Reusable):
    instance = None

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = LogoutPage()
        return cls.instance

    def __init__(self):
        super().__init__()

    def logout(self):
        time.sleep(5)
        super().perform_action_on_element(Logout.UIImage, "ClickWithActionClass")
        super().perform_action_on_element(Logout.Logout, "Click")
        # assert super().element_exists(SignInPage.Login) is True, "User Successfully Logged-out"
        time.sleep(5)

logout_page = LogoutPage.get_instance()