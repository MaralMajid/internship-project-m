Feature: Filter the off plan products

  Scenario: User can filter the off plan products by Unit price range
    Given Open Reelly url
    When Click on Sign in button
    When Input correct email address
    When Input correct password
    Then Click on continue button
    Then Click on "Off-plan" option at the left side menu
    When Verify the right page open
    Then Click on Filter
    Then Filter the products by price range from 1200000 AED
    Then Filter the products by price range to 2000000 AED
    Then Click on Apply Filter
    Then Verify the price in all cards inside the range