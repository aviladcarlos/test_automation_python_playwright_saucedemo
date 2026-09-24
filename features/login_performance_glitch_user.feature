Feature: Login Performance Glitch User

  Scenario Outline: Verify performance glitch user logins successfully by checking if they landed on the Products page.
    Given a performance glitch user is on the login page

    When the performance glitch user logins to Sauce Demo with <username> and <password>

    Then the performance glitch user should see the Products page

    Examples:
      | username                | password      |
      | performance_glitch_user | secret_sauce  |
