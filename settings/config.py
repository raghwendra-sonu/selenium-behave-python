import os
import json

class Settings(object):
    """Simple singleton class for managing and accessing settings"""

    def __init__(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'test_settings.json')) as f:
            setting = json.load(f)
            self.url = setting['url']
            self.browser = setting['browser']
            self.driver_timeout = int(setting['driver_timeout'])
            self.password = setting['password']
            self.jira_server = setting['jira_server']
            self.jira_user = setting['jira_user']
            self.jira_password = setting['jira_password']
            self.update_jira = setting['update_jira']
            self.wait_time = setting['wait_time']
            self.use_proxy = setting['use_proxy']
            self.proxy = setting['proxy']

settings = Settings()
