Feature: Products list

  Scenario Outline: Verify expected products are listed on the Products page
    Given a standard user is on the login page

    When the standard user logins to Sauce Demo with <username> and <password>
    And the standard user should see the Products page

    Then the standard user should see the following products listed:
      | expected product                  | image                                         | cost   |
      | Sauce Labs Backpack               | /assets/sauce-backpack-1200x1500-CjRW-Djj.jpg | $29.99 |
      | Sauce Labs Bike Light             | /assets/bike-light-1200x1500-DxcZRFOA.jpg     | $9.99  |
      | Sauce Labs Bolt T-Shirt           | /assets/bolt-shirt-1200x1500-mR0ldpVS.jpg     | $15.99 |
      | Sauce Labs Fleece Jacket          | /assets/sauce-pullover-1200x1500-BfbI-PSd.jpg | $49.99 |
      | Sauce Labs Onesie                 | /assets/red-onesie-1200x1500-BrSuq0ic.jpg     | $7.99  |
      | Test.allTheThings() T-Shirt (Red) | /assets/red-tatt-1200x1500-E-qp6aYf.jpg       | $15.99 |

    Examples:
      | username      | password     |
      | standard_user | secret_sauce |
