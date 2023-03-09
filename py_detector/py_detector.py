import datetime
from dotenv import dotenv_values
import json
import sys
import trackers_manager
import selenium_manager
import db_manager

config = dotenv_values(".env")


def find_trackers(events):
    """ Detect the trackers on the site """
    trackers_list = trackers_manager.get_trackers_from_exodus()

    if len(trackers_list) == 0:
        sys.stderr.write("No trackers found")
        return None

    trackers_detected = []
    # TODO: Use something more optimized than O(n^2)

    for event in events:
        for tracker in trackers_list:
            network_signature = tracker['network_signature'].replace("\\", "")
            network_signatures = network_signature.split("|")

            for network_signature in network_signatures:
                event_url = event['params']['response']['url']
                if network_signature in event_url and network_signature != "":
                    # append the tracker if it's not already in the list
                    if tracker not in trackers_detected:
                        found = tracker
                        tracker['event_url'] = [event_url]
                        trackers_detected.append(found)
                    else:
                        # append the event url to the tracker
                        trackers_detected[trackers_detected.index(
                            tracker)]['event_url'].append(event_url)

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


def navigate_site(url):
    driver = selenium_manager.init_driver(config['HEADLESS'] == 'True')
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


def main():
    url = sys.argv[1]
    if config['USE_MONGO'] == 'True':
        record = db_manager.get_stored_url(url)
        if record is not None and record['date'] > datetime.datetime.now() - datetime.timedelta(days=1):
            print(json.dumps(record['trackers'], indent=4, sort_keys=True))
            return record['trackers']
        else:
            trackers = navigate_site(url)

            if record is not None:
                db_manager.update_url(trackers, record['_id'])
            else:
                db_manager.store_url(url, trackers)
            return trackers
    else:
        return navigate_site(url)


main()
