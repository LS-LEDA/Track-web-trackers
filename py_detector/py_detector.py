import json
import sys
import trackers_manager
import selenium_manager

# Configuration TODO: move to .env file
HEADLESS = True


# TODO: Use something more optimized than O(n^2)
def find_trackers(events):
    """ Detect the trackers on the site """
    trackers_list = trackers_manager.get_trackers_from_exodus()

    if len(trackers_list) == 0:
        sys.stderr.write("No trackers found")
        return None

    trackers_detected = []

    for event in events:
        for tracker in trackers_list:
            network_signature = tracker['network_signature'].replace("\\", "")
            network_signatures = network_signature.split("|")

            for network_signature in network_signatures:
                event_url = event['params']['response']['url']
                if network_signature in event_url and network_signature != "":
                    found = tracker
                    found['event_url'] = event_url
                    trackers_detected.append(found)
                    """ TODO: Return only relevant information """

    return trackers_detected


def get_events(driver, url):
    """ Get all events from the url"""
    try:
        driver.get(url)
    except Exception as e:
        sys.stderr.write("Error getting events: " + str(e))
        return None

    events = selenium_manager.get_filtered_events(driver)
    selenium_manager.close_driver(driver)
    return events


def main():
    url = sys.argv[1]

    driver = selenium_manager.init_driver(HEADLESS)
    if driver is None:
        return
    events = get_events(driver, url)
    if events is None:
        return
    trackers = find_trackers(events)
    if trackers is None:
        return
    print(json.dumps(trackers, indent=4, sort_keys=True))

    return trackers


main()
