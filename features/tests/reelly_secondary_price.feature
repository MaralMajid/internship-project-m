Feature: Unit Price Range

  Scenario: Filter the Secondary deals by Unit price range
    Given Open Reelly url
    When Click on Sign in button
    When Input correct email address
    When Input correct password
    Then Click on continue button
    Then Click on "Secondary" option at the left side menu
    When Verify the right page opens
    Then Click on Filters
    Then Filter the products by price range from 1200000 AED
    Then Filter the products by price range to 2000000 AED
    Then Click on Apply Filter
    Then Verify the price in all cards inside the range