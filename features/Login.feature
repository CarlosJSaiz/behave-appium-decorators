Feature: Login and check price
    Login as a regular user and check product price

    Scenario: Check Login
        Given I am on Login screen
        When I insert username "standard_user" and password "secret_sauce"
        Then Products screen is displayed

    Scenario: Check baby tshirt price
        Given I am on Products screen
        When I put baby tshirt on screen
        Then The price should be "7.99"