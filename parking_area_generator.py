import random


def run(total_slots, handicapped_rate=0.3):
    data, slot, numbers = {}, {}, []
    i, j = 0, 0

    """
    * It creates a parking slot for the disabled from the total parking slot according to
    * the rate specified in the 'handicapped_rate' parameter.
    * 
    * Then, the float output is converted to integer and averaged by round.
    * For example, 2 for 1.5 and above, 1 for 1.4 and below.
    """
    handicapped_rate = total_slots * handicapped_rate
    handicapped_slot_count = int(round(handicapped_rate))

    """
    * Generate a random number. If this random number not in the list named number then not break the while loop.
    * Distance to entrance is calculated according to unique random number.
    * Distance o exit is calculated according to this subtraction: total_slots - random_number.
    * If distance to entrance value is 20st in 20, so distance to exit value is 0.
    * Because there is no valid car slot in parking. 20st is the end of 20.
    """
    while i < total_slots:
        random_number = random.randint(0, total_slots)
        if random_number not in numbers:
            numbers.append(random_number)
            slot['distance_to_entrance'] = random_number
            slot['distance_to_exit'] = total_slots - random_number
            slot['is_filled'] = False

            if j == handicapped_slot_count:
                slot['for_handicapped'] = False

            while j < handicapped_slot_count:
                slot['for_handicapped'] = True
                j = j + 1
                break

            data[i] = slot
            slot = {}
            i = i + 1

    return data


"""
* Below codes runs only in testing process. Except this those code lines are useless.
* To run below codes please import json lib.

if __name__ == '__main__':
    parking_area = create_parking_area(20, 0.5)
    parsed_json = json.loads(json.dumps(parking_area))
    output = json.dumps(parsed_json, indent=2)
    print(output)
"""