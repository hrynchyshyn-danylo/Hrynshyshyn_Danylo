Feature: Automate OrangeHRM

  Scenario: Login
    Given I navigated to the OrangeHRM website
      When I enter username as "Admin" and password as "admin123"
      And I click on login button
        Then Page should reload and I should see burger menu on the left

  Scenario: Add new job
    Given I navigated to the OrangeHRM website
      When I navigate to "Add new job" form
      And I submit "Add new job" form
        Then I should see created job in the list

  Scenario: Delete my job
    Given I navigated to job title list
      When I delete my job
        Then I should not see my job in the list
