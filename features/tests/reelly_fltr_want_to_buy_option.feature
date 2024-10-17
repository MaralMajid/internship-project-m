
Feature: Relly Secondary deals

  Scenario: Filter want to buy options
    Given Open Reelly url
    When Click on Sign in button
    When Input correct email address
    When Input correct password
    Then Click on continue button
    Then Click on "Secondary" option at the left side menu
    When Verify the right page opens
    Then Click on Filters
    Then Filter the products by "Want to buy"
    Then Click on Apply Filter
    Then Verify all cards have "want to buy" tag