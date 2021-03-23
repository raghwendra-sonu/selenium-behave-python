from behave import step
from allocator.driver import driver
from pages.home_page import HomePage
from pages.logout_page import LogoutPage
from settings.config import settings
from utilities.Jira import jira

@step(u'I set Jira TestRun ID as "{issue_key}"')
def set_jira_test_run_id(context,issue_key):
    if settings.update_jira:
        jira.connect_to_jira()
        jira.get_issue_key(issue_key)

@step('I select user role as "{role}"')
def select_role(context, role):
    try:
        HomePage().select_user_role(role)
        driver.capture_screenshot()
    except:
        LogoutPage().logout()
         #  assert reusable.element_exists(Home.user_role) is True, "User successfully selected the appropriate role"