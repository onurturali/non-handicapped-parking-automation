# non-handicapped-parking-automation
 non handicapped parking automation with virtualization.

parking_area_generator.py file generates randomly parking slots. Also parking design can be drawn.
- Handicapped slot range can be defined.
- Total slots can be defined.

car_entry_request_generator.py file generates randomly car entry requests.
- Datetime is generated according to datetime range.
- Handicapped status is randomly generated as True or False.

For more information you can read comment blocks in each files.

# Example Outputs

## car_entry_request_generator.py

{0: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:59:48', 'entry_request': 0}, 1: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:55:51', 'entry_request': 0}, 2: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:56:25', 'entry_request': 0}, 3: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:59:14', 'entry_request': 0}, 4: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:56:26', 'entry_request': 0}, 5: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:52:19', 'entry_request': 0}, 6: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:53:05', 'entry_request': 0}, 7: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:54:46', 'entry_request': 0}, 8: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:53:31', 'entry_request': 0}, 9: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:51:13', 'entry_request': 0}, 10: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:51:53', 'entry_request': 0}, 11: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:55:52', 'entry_request': 0}, 12: {'is_handicapped': False, 
'entry_datetime': '20/01/2020 23:58:11', 'entry_request': 0}, 13: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:57:16', 'entry_request': 0}, 14: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:55:39', 
'entry_request': 0}, 15: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:57:46', 'entry_request': 0}, 16: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:58:19', 'entry_request': 0}, 17: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:51:12', 'entry_request': 0}, 18: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:57:49', 'entry_request': 0}, 19: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:59:27', 'entry_request': 0}, 20: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:50:07', 'entry_request': 0}, 21: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:51:09', 'entry_request': 0}, 22: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:53:02', 'entry_request': 0}, 23: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:56:25', 'entry_request': 0}, 24: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:59:44', 'entry_request': 0}, 25: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:55:15', 'entry_request': 0}, 26: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:51:46', 'entry_request': 0}, 
27: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:57:56', 'entry_request': 0}, 28: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:55:51', 'entry_request': 0}, 29: {'is_handicapped': False, 'entry_datetime': '20/01/2020 23:51:18', 'entry_request': 0}}

## parking_lot_generator.py

{0: {'distance_to_entrance': 3, 'distance_to_exit': 17, 'is_filled': False, 'for_handicapped': True}, 1: {'distance_to_entrance': 5, 'distance_to_exit': 15, 'is_filled': False, 'for_handicapped': True}, 2: {'distance_to_entrance': 4, 'distance_to_exit': 16, 'is_filled': False, 'for_handicapped': True}, 3: {'distance_to_entrance': 6, 'distance_to_exit': 14, 'is_filled': False, 'for_handicapped': True}, 4: {'distance_to_entrance': 13, 'distance_to_exit': 7, 'is_filled': False, 'for_handicapped': True}, 5: {'distance_to_entrance': 11, 'distance_to_exit': 9, 'is_filled': False, 'for_handicapped': True}, 6: {'distance_to_entrance': 9, 'distance_to_exit': 11, 'is_filled': 
False, 'for_handicapped': True}, 7: {'distance_to_entrance': 2, 'distance_to_exit': 18, 'is_filled': False, 'for_handicapped': True}, 8: {'distance_to_entrance': 12, 'distance_to_exit': 8, 'is_filled': False, 'for_handicapped': True}, 9: {'distance_to_entrance': 15, 'distance_to_exit': 5, 'is_filled': False, 'for_handicapped': True}, 10: {'distance_to_entrance': 0, 'distance_to_exit': 20, 'is_filled': False, 'for_handicapped': False}, 11: {'distance_to_entrance': 16, 'distance_to_exit': 4, 'is_filled': False, 'for_handicapped': False}, 12: {'distance_to_entrance': 10, 'distance_to_exit': 10, 'is_filled': False, 'for_handicapped': False}, 13: {'distance_to_entrance': 
1, 'distance_to_exit': 19, 'is_filled': False, 'for_handicapped': False}, 14: {'distance_to_entrance': 8, 'distance_to_exit': 12, 'is_filled': False, 'for_handicapped': False}, 15: {'distance_to_entrance': 14, 'distance_to_exit': 6, 'is_filled': False, 'for_handicapped': False}, 16: {'distance_to_entrance': 18, 'distance_to_exit': 2, 'is_filled': False, 'for_handicapped': False}, 17: {'distance_to_entrance': 7, 'distance_to_exit': 13, 'is_filled': False, 'for_handicapped': False}, 18: {'distance_to_entrance': 19, 'distance_to_exit': 1, 'is_filled': False, 'for_handicapped': False}, 19: {'distance_to_entrance': 20, 'distance_to_exit': 0, 'is_filled': False, 'for_handicapped': False}}

## slot_type_seperator.py

[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]