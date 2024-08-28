
Feature: Reelly sign in feature

  Scenario: Verify Sign in
    Given Open Reelly url
    When Click on Sign in button
    When Input correct email address
    When Input correct password
    Then Click on continue button
    Then Verify that main  page



