Feature: Login Standard User

  Scenario Outline: Verify standard user logins successfully by checking if they landed on the Products page.
    Given a standard user is on the login page

    When the standard user logins to Sauce Demo with <username> and <password>

    Then the standard user should see the Products page

    Examples:
      | username       | password      |
      | standard_user | secret_sauce  |
