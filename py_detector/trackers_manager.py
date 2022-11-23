import requests
import json
import sys


def get_trackers_from_exodus():
    """ Gets the trakers from the api of exodus """
    try:
        response = requests.get(
            'https://reports.exodus-privacy.eu.org/api/trackers')
        trackers_list = json.loads(response.text)
        return map_trackers(trackers_list['trackers'])

    except Exception as e:
        sys.stderr.write("Error getting trackers: " + str(e))
        return None


def map_trackers(trackers_list):
    """ Turn the response from exodus to a more practical format """
    trackers = []
    for tracker_index in trackers_list:
        tracker = trackers_list[tracker_index]
        trackers.append(tracker)
    return trackers


def get_trackers_from_db():
    """ Gets the trackers from the database"""
    # TODO:
    trackers = {}
    return trackers


def update_trackers_from_db(trackers):
    """ Update and add trackers to database """
    # TODO:
    return
