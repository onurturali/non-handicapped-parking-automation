from random import choice
import slot_type_seperator
import parking_lot_generator
import car_entry_request_generator
import colors

"""
* filled_slots contains two list inside.
* Because of that there are two types parking slots. Handicapped and nonhandicapped.
* index 0 is handicapped and index 1 is nonhandicapped.
"""

print('\n\n', colors.selector.VIOLET, 'The autonomous system started working...', colors.selector.END, '\n\n')

def run():
    parking_lot = parking_lot_generator.run(10, 0.5)
    handicapped_slots = slot_type_seperator.run(parking_lot, 'handicapped')
    nonhandicapped_slots = slot_type_seperator.run(parking_lot, 'nonhandicapped')
    car_req = car_entry_request_generator.run(['20/1/2020 23:50:00', '21/1/2020 00:00:00'], 30)

    is_handicapped, selected_slot, i = None, 0, 0
    car_in_lot, filled_slots = [], {'handicapped': [], 'nonhandicapped': []}

    color_end = colors.selector.END
    
    messages = {
        'handicapped': {
            'slot_found': colors.selector.GREEN + '[OK]' + color_end + ' Free handicapped slot(s) found in parking lot.',
            'no_free_slot': colors.selector.RED + '[ERROR]' + color_end + ' Free handicapped slot(s) not found in parking lot.',
        },

        'nonhandicapped': {
            'slot_found': colors.selector.GREEN + '[OK]' + color_end + ' Free nonhandicapped slot(s) found in parking lot.',
            'no_free_slot': colors.selector.RED + '[ERROR]' + color_end + ' Free nonhandicapped slot(s) not found in parking lot.',
        }
    }
    
    slot_type = ''
    tmp_list = []

    while i < len(car_req):
        # Get the driver handicap status
        is_handicapped = car_req[i]['is_handicapped']

        # Is there any free slot for handicapped or nonhandicaped drivers?
        tmp_list = handicapped_slots if is_handicapped else nonhandicapped_slots
        slot_type = 'handicapped' if is_handicapped else 'nonhandicapped'
        
        # Remove filled slot id from list (handicapped_slots or nonhandicapped_slots)
        # Add car request id to car_in_lot list
        # Add removed slot id to filled_slots
        if len(tmp_list) != 0:
            print(messages[slot_type]['slot_found'])
            print(f'Free {slot_type} slot(s) count: ', len(tmp_list))
            print(f'Free {slot_type} slots: {tmp_list}')
            print('\n')
            selected_slot = choice(tmp_list)
            tmp_list.remove(selected_slot)
            car_in_lot.append(i)
            filled_slots[slot_type].append(selected_slot)

            print('Car ID: ', i)
            print('Selected slot: {0}'.format(selected_slot))
            print(f'Car id in lot: {car_in_lot}')
            print(f'Filled slots: {filled_slots[slot_type]}')
        else:
            print(messages[slot_type]['no_free_slot'])
            print('Car ID: ', i)
        print('\n', '-'*50, '\n')
        i = i + 1

print(run())