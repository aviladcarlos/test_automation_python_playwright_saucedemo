Feature: Login Locked Out User

  Scenario Outline: Verify locked out message is displayed when user attempts to login with a locked out user.
    Given a locked out user is on the login page

    When the locked out user logins to Sauce Demo with <username> and <password>

    Then the locked out user should see the locked out message
    And the locked out user should remain on the login page after locked out message is displayed

    Examples:
      | username       | password      |
      | locked_out_user | secret_sauce  |
