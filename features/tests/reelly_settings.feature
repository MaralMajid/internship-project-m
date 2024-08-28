
Feature: Setting

  Scenario: User can open User Guide page
    Given Open Reelly url
    When Click on Sign in button
    When Input correct email address
    When Input correct password
    Then Click on continue button
    Then Click on Setting button
    When Click on User Guide button
    Then Verify that right page opens
    Then Verify all lesson videos contain title
