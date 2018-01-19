# coursemonitor

This WIP Python 2 module monitors the status of Cornell classes based on the Course Roster.

## Installation

- Run `pip install -r requirements.txt` to install the required dependencies for this package.
- Edit `.env_template` with your own values for Twilio, and run `source .env_template` from your terminal.


## TODO

- Changing refresh times according to Course Roster (every 10 mins, 20 mins, or 1 hr based on time of day)
- Sending SMS messages when course is Open.