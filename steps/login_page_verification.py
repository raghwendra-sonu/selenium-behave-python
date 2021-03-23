from behave import step
from pages.login_page import LoginPage
from pages.logout_page import LogoutPage
from settings.config import settings
from allocator.driver import driver

@step(u'I navigate to Salesforce website')
def load_website(context):
    try:
        driver.navigate(settings.url)
        driver.capture_screenshot()
    except:
        LogoutPage().logout()

@step(u'I login with "{role}" and "{username}"')
def login_step(context, role, username):
    try:
        LoginPage().login(username, settings.password+role)
        LoginPage().verify_user_loggedin(username)
        driver.capture_screenshot()
    except:
        LogoutPage().logout()