from behave import step
from allocator.driver import driver
from pages.logout_page import LogoutPage

@step(u'I logout from Salesforce website')
def logout(context):
    LogoutPage().logout()
    driver.capture_screenshot()
