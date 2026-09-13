Feature: Login Standard User

  Scenario Outline: Verify standard user logins successfully by checking if they landed on the Products page.
    Given I am a standard user on the login page

    When I login to Sauce Demo with <username> and <password>

    Then I should see the Products page

    Examples:
      | username       | password      |
      | standard_user | secret_sauce  |
