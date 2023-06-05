Feature: Test EPAM website

  Scenario: Verify Navigation menu buttons
    Given I navigated to homepage
      Then I should see 6 navigation buttons : "Services", "Industries", "Insights", "About", "Careers"

  Scenario: Verify Services Page Title
    Given I navigated to homepage
      When I click on "Services" button
      And I see "Services" page is loaded
      And I retrieve title of the page
        Then Title of page is "Services | EPAM"

  Scenario: Use search to find "Contacts" page
    Given I navigated to homepage
      When I click on the search icon
      And I enter "Contacts" in the search bar
      And I click on submit button
        Then The first search result is "Contact Us" with appropriate url

  Scenario: Switch to Polish language and verify page title
    Given I navigated to homepage
      When I click on the language selector in the header
      And I select "Polska" language
        Then I am redirected to Polish homepage and its title is 'EPAM | Praca dla doświadczonych specjalistów IT'

  Scenario: Navigate to About Page
    Given I navigated to homepage
      When I click on the "About" button in the navigation menu
        Then I should be redirected to "About" page

  Scenario: Verify Social Media Links
    Given I navigated to homepage
      When I scroll to the bottom of the page
        Then I should see icons with appropriate links for "Linkedin", "Facebook", "Twitter", "Instagram", "Youtube", and "Glassdoor" in the footer

  Scenario: Open Side Menu
    Given I navigated to homepage
      When I click on side menu button
        Then I should see a side menu after a second

  Scenario: Open contacts page
    Given I navigated to homepage
      When I click on the "Contact" link in the navigation menu
        Then I should be redirected to "Contact" page

  Scenario: Verify Cookies options menu presence when cookies are deleted
    Given I navigated to homepage
      When I delete cookies
      And I go to homepage
        Then I should see a cookies options menu in few seconds
