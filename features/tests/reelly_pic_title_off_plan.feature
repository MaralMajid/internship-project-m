Feature: Visibility of pictures and titles on each product

  Scenario: User can see titles and pictures on each product inside the off plan page
    Given Open Reelly url
    When Click on Sign in button
    When Input correct email address
    When Input correct password
    Then Click on continue button
    Then Click on "Off-plan" option at the left side menu
    When Verify the right page open
    Then Verify each product on this page contains a title and picture visible