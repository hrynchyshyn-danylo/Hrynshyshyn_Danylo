from typing import Optional
from selenium.common import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from behave import given, when, then
import chromedriver_autoinstaller
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib3.exceptions import MaxRetryError

chromedriver_autoinstaller.install()


# Verify Homepage Title
@given('I navigated to homepage')
def step_given_on_homepage(context):
    context.browser.get('https://www.epam.com/')

@then('I should see 6 navigation buttons : "Services", "Industries", "Insights", "About", "Careers"')
def step_then_check_navigation_buttons(context):
    navigation_buttons = context.browser.find_elements(By.CLASS_NAME, 'top-navigation__item-link')
    expected_names = ['Services', 'Industries', 'Insights', 'About', 'Careers']
    button_names = [button.text for button in navigation_buttons]
    assert button_names == expected_names, f'Expected names: {expected_names = }, Actual names: {button_names = }'


@when('I delete cookies')
def step_when_delete_cookies(context):
    context.browser.delete_all_cookies()

@when('I go to homepage')
def step_then_go_to_homepage(context):
    context.browser.get('https://www.epam.com/')

@then('I should see a cookies options menu in few seconds')
def step_then_check_cookies_options_menu(context):
    try :
        WebDriverWait(context.browser, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div/div[6]/div[2]/div/div[1]/div/div[2]/div/button[2]'))
        )
    finally :
        context.browser.quit()

@when('I click on "Services" button')
def step_when_click_services_button(context):
    context.browser.find_element(By.LINK_TEXT, 'Services').click()

@when('I see "Services" page is loaded')
def step_then_check_services_page(context):
    WebDriverWait(context.browser, 10).until(
        EC.url_to_be('https://www.epam.com/services')
    )

@when('I retrieve title of the page')
def step_when_retrieve_page_title(context):
    context.title = context.browser.title

@then('Title of page is "Services | EPAM"')
def step_then_check_title(context):
    assert context.title == 'Services | EPAM'

@when('I click on the search icon')
def step_when_click_search_icon(context):
    context.browser.find_element(By.CLASS_NAME, 'header-search__button').click()

@when('I enter "Contacts" in the search bar')
def step_when_enter_contacts(context):
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.ID, 'new_form_search'))
    )
    context.browser.find_element(By.ID, 'new_form_search').send_keys('Contacts')

@when('I click on submit button')
def step_given_click_submit(context):
    context.browser.find_element(By.CLASS_NAME, 'header-search__submit').click()

@then('The first search result is "Contact Us" with appropriate url')
def step_then_check_first_search_result(context):
    search_results = context.browser.find_elements(By.CLASS_NAME, 'search-results__title-link')
    href = search_results[0].get_property('href')
    assert href == 'https://www.epam.com/about/who-we-are/contact'

@when('I click on the language selector in the header')
def step_when_click_language_selector(context):
    context.browser.find_element(By.CLASS_NAME, 'location-selector__button').click()
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'location-selector__item'))
    )

@when('I select "Polska" language')
def step_given_select_polish_language(context):
    # find a by href='https://careers.epam-poland.pl/
    context.browser.find_element(By.XPATH, '//li[@class="location-selector__item"]/a[@href="https://careers.epam-poland.pl"]').click()


@then("I am redirected to Polish homepage and its title is 'EPAM | Praca dla doświadczonych specjalistów IT'")
def step_then_check_polish_homepage(context):
    WebDriverWait(context.browser, 10).until(
        EC.url_to_be('https://careers.epam-poland.pl/')
    )
    assert context.browser.title == 'EPAM | Praca dla doświadczonych specjalistów IT'

@when('I click on the "About" button in the navigation menu')
def step_when_click_about_button(context):
    context.browser.find_element(By.LINK_TEXT, 'About').click()

@then('I should be redirected to "About" page')
def step_then_check_about_page(context):
    WebDriverWait(context.browser, 10).until(
        EC.url_to_be('https://www.epam.com/about')
    )

@when('I scroll to the bottom of the page')
def step_when_scroll_to_bottom(context):
    context.browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")

@then('I should see icons with appropriate links for "Linkedin", "Facebook", "Twitter", "Instagram", "Youtube", and "Glassdoor" in the footer')
def step_then_check_social_media_links(context):
    social_media_links = context.browser.find_elements(By.XPATH, '//div[@class="social"]//a')
    hrefs = [link.get_property('href') for link in social_media_links]
    expected_hrefs = [
        'https://www.linkedin.com/company/epam-systems/',
        'https://twitter.com/EPAMSYSTEMS',
        'https://www.facebook.com/EPAM.Global',
        'https://www.instagram.com/epamsystems/',
        'https://www.youtube.com/c/EPAMSystemsGlobal'
    ]
    assert hrefs == expected_hrefs, f'{hrefs = }, {expected_hrefs = }'


@when('I click on side menu button')
def step_when_click_side_menu_button(context):
    context.browser.find_element(By.CLASS_NAME, 'hamburger-menu__button').click()

@then('I should see a side menu after a second')
def step_then_check_side_menu(context):
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'os-content'))
    )

@when('I click on the "Contact" link in the navigation menu')
def step_when_click_contact_link(context):
    context.browser.find_element(By.LINK_TEXT, 'CONTACT US').click()

@then('I should be redirected to "Contact" page')
def step_then_check_contact_page(context):
    WebDriverWait(context.browser, 10).until(
        EC.url_to_be('https://www.epam.com/about/who-we-are/contact')
    )












