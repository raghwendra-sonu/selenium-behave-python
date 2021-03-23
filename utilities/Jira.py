from jira.client import JIRA
from allocator.reusableLibrary import Reusable
from settings.config import settings

class Jira_utility(Reusable):
    instance = None
    jira = ""
    issue = ""
    execution_status = ""

    @classmethod
    def get_instance(cls):
        if cls.instance is None:
            cls.instance = Jira_utility()
        return cls.instance

    def connect_to_jira(context):
        jira_server = {'server': settings.jira_server}
        global jira
        if settings.use_proxy:
            jira = JIRA(options=jira_server, basic_auth=(settings.jira_user, settings.jira_password), proxies={"http": "http://zscaler.test.com:80", "https": "https://zscaler.star.com.au:80"})
        else:
            jira = JIRA(options=jira_server, basic_auth=(settings.jira_user, settings.jira_password))

    def get_issue_key(context, issue_key):
        global issue
        issue = jira.issue(issue_key)

    def get_execution_status(context, status):
        global execution_status
        execution_status = status

    def transition_issue(context):
        jira.transition_issue(issue, transition='Ready For Test')
        jira.transition_issue(issue, transition='Test in Progress')
        jira.transition_issue(issue, transition=execution_status)

    def attach_screenshots_in_jira(context, attachment_path):
        # for attachment in issue.fields.attachment:
        #     jira.delete_attachment(attachment['id'])
        jira.add_attachment(issue=issue, attachment=attachment_path)

    def add_comment(context):
        list_of_comments = jira.comments(issue)
        if len(list_of_comments) > 0:
            for comment in list_of_comments:
                comment.delete()
        jira.add_comment(issue, 'Automated Test Execution Reports available at Jenkins ->"http://localhost:8080/job/Patron/"')


jira = Jira_utility.get_instance()
