from typing import Optional
from selenium.common import WebDriverException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from urllib3.exceptions import MaxRetryError


@given('I navigated to the OrangeHRM website')
def step_given_navigate_to_orangehrm(context):
    context.browser.get('https://opensource-demo.orangehrmlive.com/')
    WebDriverWait(context.browser, 10).until(
        EC.title_is('OrangeHRM')
    )

# when I enter username as "Admin" and password as "admin123"
@when('I enter username as "Admin" and password as "admin123"')
def step_when_enter_username_and_password(context):
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.NAME, 'username'))
    )
    context.browser.find_element(By.NAME, 'username').send_keys('Admin')
    context.browser.find_element(By.NAME, 'password').send_keys('admin123')

# and I click on login button
@when('I click on login button')
def step_when_click_login_button(context):
    context.browser.find_element(By.CLASS_NAME, 'orangehrm-login-action').click()

# then Page should reload and I should see burger menu on the left
@then('Page should reload and I should see burger menu on the left')
def step_then_check_burger_menu(context):
    WebDriverWait(context.browser, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, 'oxd-navbar-nav'))
    )

@when('I navigate to "Add new job" form')
def step_when_navigate_to_add_new_job_form(context):
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//li[contains(., "Admin")]'))
    ).click()
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'oxd-topbar-body-nav-tab'))
    )
    context.browser.find_elements(By.CLASS_NAME, 'oxd-topbar-body-nav-tab')[1].click()
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.CLASS_NAME, 'oxd-dropdown-menu'))
    )
    context.browser.find_elements(By.XPATH, '//ul[@class="oxd-dropdown-menu"]//li')[0].click()
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(., " Add ")]'))
    ).click()

# and I submit "Add new job" form
@when('I submit "Add new job" form')
def step_when_submit_add_new_job_form(context):
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//input[contains(@class, 'oxd-input')]"))
    )
    context.browser.find_elements(By.XPATH, "//input[contains(@class, 'oxd-input')]")[1].send_keys('QA Intern #123465')
    context.browser.find_elements(By.TAG_NAME, 'textarea')[0].send_keys('QA Intern #123465')
    context.browser.find_elements(By.TAG_NAME, 'textarea')[1].send_keys('QA Intern #123465')
    # button type=submit click immediate
    context.browser.find_element(By.XPATH, '//button[@type="submit"]').click()

# then I should see created job in the list
@then('I should see created job in the list')
def step_then_check_created_job(context):
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@class="oxd-table-card" and contains(., "QA Intern #123465")]'))
    )

# given I navigated to admin panel of OrangeHRM
@given('I navigated to job title list')
def step_given_navigate_to_admin_panel(context):
    context.browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList')
    WebDriverWait(context.browser, 10).until(
        EC.title_is('OrangeHRM')
    )

# when I delete my job
@when('I delete my job')
def step_when_delete_my_job(context):
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//div[@class="oxd-table-card" and contains(., "QA Intern #123465")]//button[@class="oxd-icon-button oxd-table-cell-action-space"][1]'))
    ).click()
    # wait and  click on //*[@id="app"]/div[3]/div/div/div/div[3]/button[2]
    WebDriverWait(context.browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[contains(., " Yes, Delete ")]'))
    ).click()

@then('I should not see my job in the list')
def step_then_check_deleted_job(context):
    context.browser.get('https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewJobTitleList')
    # wait until at least one suck card appears
    WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@class="oxd-table-card"]'))
    )
    # assert that this job is not on the list
    assert len(context.browser.find_elements(By.XPATH, '//div[@class="oxd-table-card" and contains(text(), "QA Intern #123465")]')) == 0





