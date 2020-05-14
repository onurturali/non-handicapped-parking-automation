import random
import parking_lot_generator as lot_generator
import car_entry_request_generator as entry_generator

"""
* Values must be seperated to commit, display, merge, group, separate and delete.
* Parking lot data comes from parking_lot_generator file into here.
* In this file, handicapped and non-handicapped slots seperate into different lists.
* 
* handicapped_slots contains only id.
* nonhandicapped_slots contains only id.
* 
* To instance, when handicapped driver wants to enter into parking lot,
* Slot ids will be searched in those lists.
* 
* Important parameters and values to use and define:
* 
* handicapped_slots list
* nonhandicapped_slots list
* lost parking_lot_generator.run
"""

def run(parking_lot_function, type):
    lot = parking_lot_function
    handicapped_slots = []
    nonhadicapped_slots = []

    for parent_key, parent_value in lot.items():
        for child_key, child_value in parent_value.items():
            if child_key == 'for_handicapped':
                if child_value:
                    handicapped_slots.append(parent_key)
                else:
                    nonhadicapped_slots.append(parent_key)
    
    if type == 'handicapped':
        return handicapped_slots
    elif type == 'nonhandicapped':
        return nonhadicapped_slots
    else:
        return False
    
"""
* Below codes runs only in testing process. Except this those code lines are useless.

if __name__ == '__main__':
    print(run(lot_generator.run(20, 0.5), 'nonhandicapped'))
"""