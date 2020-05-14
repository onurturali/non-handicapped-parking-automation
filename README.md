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

{
  "0": {
    "is_handicapped": true,
    "entry_datetime": "03/01/2020 05:13:55",
    "entry_request": 0
  },
  "1": {
    "is_handicapped": true,
    "entry_datetime": "12/01/2020 14:16:02",
    "entry_request": 0
  },
  "2": {
    "is_handicapped": true,
    "entry_datetime": "16/01/2020 00:17:34",
    "entry_request": 0
  },
  "3": {
    "entry_datetime": "18/02/2020 13:26:07",
    "entry_request": 0
  },
  "4": {
    "is_handicapped": true,
    "entry_datetime": "07/02/2020 15:54:28",
    "entry_request": 0
  }
}