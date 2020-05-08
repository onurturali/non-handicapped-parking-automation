import random
from random import randrange
from datetime import timedelta
from datetime import datetime

"""
* Bugs most be fixed:
* A different clock system is not possible on the same day.
* 
* entry_request meanings:
* It can not be changed at first.
* 'no_req' means no entry request for now
* 'req_and_access' means request accessed
* 'req_but_fail' means request denied. scenarios: parking slots are full or no perticular parking slot
* 
* datetime_range meaning:
* default format is %d/%m/%Y %H:%M:%S | Test based: days/months/years hours:minutes:seconds
* If you want to chande default datetime format in parameter, pass suited parameter while calling it
* The end day in date format must be one day ahead. A different clock system is not possible on the same day.
* 
* The function below named run, generates randomly is_handicapped value. It generates just True or just False.
"""


def run(datetime_range, datetime_format='%d/%m/%Y %H:%M:%S'):
    start = datetime.strptime(datetime_range[0], datetime_format)
    end = datetime.strptime(datetime_range[1], datetime_format)
    is_handicapped = random.choice([True, False])

    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    entry_datetime = datetime.strftime(start + timedelta(seconds=random_second), datetime_format)

    car_req_data = {'is_handicapped': is_handicapped, 'entry_datetime': entry_datetime, 'entry_request': 0}

    return car_req_data


"""
* Below codes runs only in testing process. Except this those code lines are useless.
"""
if __name__ == '__main__':
    car_entry_req = run(['20/1/2020 23:50:00', '21/1/2020 00:00:00'])
    print(car_entry_req)


