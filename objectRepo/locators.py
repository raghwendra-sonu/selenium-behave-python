from selenium.webdriver.common.by import By

class Locator:
    def __init__(self, l_type, selector):
        self.l_type = l_type
        self.selector = selector

    def parameterize(self, *args):
        self.selector = self.selector.format(*args)

class AppLauncher:
    AppLauncher = Locator(By.XPATH, "//div[@class='slds-icon-waffle']")

class SignInPage:
    UserName = Locator(By.XPATH, "//input[@id='username']")
    Password = Locator(By.XPATH, "//input[@id='password']")
    Login = Locator(By.XPATH, "//input[@id='Login']")
    login_popup = Locator(By.XPATH, "//*[text()='Log In']")

class Logout:
    UIImage = Locator(By.XPATH,"//img[@title='User']")
    Logout = Locator(By.XPATH,"//a[text()='Log Out']")

class Home:
    new_account_tab = Locator(By.XPATH, "//a[@title='Accounts']//following-sibling::one-app-nav-bar-item-dropdown//*[name()='svg']")
    NewAccount = Locator(By.XPATH,"//span[text()='New Account']")
    account_name_txtbox_new_account_window = Locator(By.XPATH,"//span[text()='Account Name']//parent::label//following-sibling::div//input")
    salesforce_save_btn_NewAccountWindow = Locator(By.XPATH,"//button[@title='Save']")
    salesforce_name_of_new_account = Locator(By.XPATH,"//slot[@name='primaryField']//div//span[contains(text(),'ObjectToken')]")
    dynamic_text = Locator(By.XPATH, "(//*[text()='ObjectToken'])[1]")
    primitive_icon = Locator(By.XPATH,"(//a[@title='ObjectToken']/parent::span/parent::th/following-sibling::td[3]//lightning-primitive-icon)[1]")
    delete = Locator(By.XPATH,"//a[@title='Delete']")
    delete_popup = Locator(By.XPATH,"//span[text()='Delete']")
    AppLauncher = Locator(By.XPATH, "//div[@class='slds-icon-waffle']")
    view_all_link = Locator(By.XPATH, "//button[text()='View All']")
    user_role = Locator(By.XPATH, "//span[@title='IRB']")
    Role = Locator(By.XPATH, "(//p[text()='ObjectToken'])")