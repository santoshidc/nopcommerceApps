import pytest
from selenium import webdriver

@pytest.fixture()
def setup(browser):
    if browser == None:
        driver = webdriver.Chrome()
    if browser.lower() == 'chrome':
        driver = webdriver.Chrome()
        print("Launching Chrome Browser")
    elif browser.lower() == 'firefox':
        driver = webdriver.Firefox()
        print("Launching Firefox Browser")
    else:
        driver = webdriver.Ie()
    return driver

def pytest_addoption(parser):  # This will get the value from CLI / hooks
    parser.addoption("--browser")

@pytest.fixture()
def browser(request): #This will return the browser value to setup method
    return request.config.getoption("--browser")

########## Py test HTML Report    ####################

def pytest_configure(config):
    config._metadata["Project Name"] = 'Windows System Security'
    config._metadata['Module Name'] = 'Customer'
    config._metadata['Tester'] = 'Santosh'

## It is hook for delete / modify environment info to HTML Report

@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)