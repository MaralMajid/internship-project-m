Feature: Sale status Out of Stocks

  Scenario: User can filter by sale status Out of Stocks
    Given Open Reelly url
    When Click on Sign in button
    When Input correct email address
    When Input correct password
    Then Click on continue button
    Then Click on "Off-plan" option at the left side menu
    When Verify the right page open
    Then Click on Sales status
    Then Filter by sale status of “Out of Stocks”
    Then Verify each product contains the Out of Stocks tag