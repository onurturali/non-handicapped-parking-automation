# non-handicapped-parking-automation
 non handicapped parking automation with virtualization.

 ## How it works?
 1. The parking lot automatically creates itself by respecting the handicapped / nonhandicapped lot ratio.
 2. Car entry requests are create within a certain date range, also.
 3. If there is still room available for handicapped or nonhandicapped, vehicles start to enter the parking lot in order.

 ## What is being done now?
 1. Cars exit the parking lot.

# About functions
parking_area_generator.py file generates randomly parking slots. Also parking design can be drawn.
- Handicapped slot range can be defined.
- Total slots can be defined.

car_entry_request_generator.py file generates randomly car entry requests.
- Datetime is generated according to datetime range.
- Handicapped status is randomly generated as True or False.

For more information you can read comment blocks in each files.

# Example Outputs

## car_entry_request_generator.py

{ 0: {
        'is_handicapped': False,
        'entry_datetime': '20/01/2020 23:59:48',
        'entry_request': 0
    }
}

## parking_lot_generator.py

{ 0: {
        'distance_to_entrance': 3,
        'distance_to_exit': 17,
        'is_filled': False,
        'for_handicapped': True
    }
}

## slot_type_seperator.py

[10, 11, 12, 13, 14, 15, 16, 17, 18, 19]