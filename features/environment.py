from selenium import webdriver
import chromedriver_autoinstaller
chromedriver_autoinstaller.install()

def before_all(context):
    context.browser = webdriver.Chrome()
    context.browser.maximize_window()

def after_all(context):
    context.browser.quit()
