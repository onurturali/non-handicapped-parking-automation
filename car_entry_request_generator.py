import random

"""
* entry_request meanings:
* 
* 'no_req' means no entry request for now
* 'req_and_access' means request accessed
* 'req_but_fail' means request denied. scenarios: parking slots are full or no perticular parking slot 
"""


def run(is_driver_handicapped, entry_time, entry_date):
    """
    :param is_driver_handicapped:
    :param entry_time:
    :param entry_date:
    :return:
    """
    driver_data = {
        'handicapped': is_driver_handicapped,
        'entry_time': entry_time,
        'entry_date': entry_date,
        'entry_request': 0
    }

    return driver_data
