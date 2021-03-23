Feature: View existing patrons for IRB & IPM users

  @Regression
  Scenario Outline: Navigate to existing Patron through IRB & IPM users
    Given I set Jira TestRun ID as "<TestRunID>"
    When I navigate to Salesforce website
    And I login with "<role>" and "<username>"
    And I select user role as "<user_role>"
    And I logout from Salesforce website

    Examples:
      | username                 | TestRunID | user_role | PatronName | role |
      | testirb@test.com.au.sit  | CRMU-976  | IRB       | Automation | irb  |
      | test_ipm@test.com.au.sit | CRMU-1042 | IPM       | Automation | ipm  |