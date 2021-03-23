from allocator.driver import driver
from settings.config import settings
from utilities.Jira import jira
from behave.model_core import Status
from pages.logout_page import LogoutPage

def after_all(context):
    driver.stop_instance()

def before_scenario(context, scenario):
    driver.clear_cookies()

def after_step(context, step):
    if settings.update_jira:
        if step.status == "failed":
            driver.capture_screenshot()
            jira.attach_screenshots_in_jira(driver.capture_screenshots_for_jira())
            LogoutPage().logout()

def after_scenario(context, scenario):
    print(scenario.status)
    if settings.update_jira:
        if scenario.status == Status.failed:
            status = "Fail"
        else:
            status = "Pass"
        jira.get_execution_status(status)
        jira.transition_issue()
        jira.add_comment()
