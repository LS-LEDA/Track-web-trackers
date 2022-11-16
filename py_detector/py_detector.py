import json

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Configuration TODO: move to .env file
HEADLESS = False
STORE_LOGS = True
STORE_RESULTS = True


# Enable browser logging
def init_driver():
    """ Inicilize the driver and return it """
    # logs
    caps = DesiredCapabilities.CHROME
    caps['goog:loggingPrefs'] = {'performance': 'ALL'}  # type: ignore

    # headless
    options = webdriver.ChromeOptions()
    if (HEADLESS):
        options.add_argument('--headless')

    # init driver
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


def gtag_tracker(events):
    """ Check if the page has a gtag tracker """
    filtered_events = [
        event for event in events if 'params' in event and 'response' in event['params']]

    for event in filtered_events:
        if 'gtag' in event['params']['response']['url']:
            return True
    return False


def get_logs(driver):
    """ Get the browser logs """
    browser_log = driver.get_log('performance')
    events = [process_browser_log_entry(entry) for entry in browser_log]
    events = [event for event in events if 'Network.response' in event['method']]
    return events


def store_logs(events, url):
    """ Store the browser logs """
    with open('logs/' + url.replace('https://', '').replace('http://', '').replace('/', '') + '.json', 'w') as outfile:
        json.dump(events, outfile, indent=4, sort_keys=True)


def search_for_trackers(driver, url):
    """ Search for trackers in the page """
    trackers = {}

    try:
        driver.get(url)

    except Exception as e:
        trackers['Error'] = "Unable to Analize the page"
        trackers['Error Message'] = str(e)
        trackers['e_code'] = 1
        return trackers

    events = get_logs(driver)

    if (gtag_tracker(events)):
        trackers['gtag'] = True
    else:
        trackers['gtag'] = False

    if (STORE_LOGS):
        store_logs(events, url)

    return trackers


def store_results(trackers, url):
    """ Store the results on a file """
    with open('results/' + url.replace('https://', '').replace('http://', '').replace('/', '') + '.json', 'w') as outfile:
        json.dump(trackers, outfile, indent=4, sort_keys=True)


def main():
    finish = 0

    # TODO: Run the script from a backend
    while (finish == 0):
        url = input("Enter URL: ")

        # if url dont has http or https
        if not (url.startswith('http://') or url.startswith('https://')):
            url = 'http://' + url

        url = url + '/'

        driver = init_driver()
        trackers = search_for_trackers(driver, url)
        close_driver(driver)
        if (STORE_RESULTS):
            store_results(trackers, url)
        print(url + " trackers: " + json.dumps(trackers, indent=4, sort_keys=True))

        finish = -1
        while (finish == -1):
            exit_input = input("Exit? (Y/n): ")
            if (exit_input == 'Y'):
                finish = 1
            elif (exit_input == 'y'):
                finish = 1
            elif (exit_input == 'N'):
                finish = 0
            elif (exit_input == 'n'):
                finish = 0
            else:
                print("Invalid input")

    print("Exiting...")


main()
