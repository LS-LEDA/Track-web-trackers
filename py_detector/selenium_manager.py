import json
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# Enable browser logging
def init_driver(headless: bool):
    """ Inicilize the driver and return it """
    # logs
    caps = DesiredCapabilities.CHROME
    caps['goog:loggingPrefs'] = {'performance': 'ALL'}  # type: ignore

    # headless
    options = webdriver.ChromeOptions()
    if (headless):
        options.add_argument('--headless')

    # do not print logs
    options.add_argument('--log-level=4')

    driver = webdriver.Chrome(desired_capabilities=caps, options=options)
    driver.implicitly_wait(10)
    return driver


def close_driver(driver):
    """ Close the driver """
    driver.quit()


def process_browser_log_entry(entry):
    """ Process the browser log entry """
    response = json.loads(entry['message'])['message']
    return response


def get_events(driver):
    """ Get the browser logs """
    browser_log = driver.get_log('performance')
    events = [process_browser_log_entry(entry) for entry in browser_log]
    events = [event for event in events if 'Network.response' in event['method']]
    return events


def get_filtered_events(driver):
    """ Filters the events that have a response """
    events = get_events(driver)
    filtered_events = [
        event for event in events if 'params' in event and 'response' in event['params']]

    return filtered_events
