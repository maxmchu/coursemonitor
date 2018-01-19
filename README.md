# coursemonitor

This Python 2 module monitors the status of Cornell classes based on the Course Roster, and can
send a SMS to your phone when a class is detected as open.

## Installation

- Run `pip install -r requirements.txt` to install the required dependencies for this package.
- Edit `.env_template` with your own values for Twilio, and run `source .env_template` from your terminal.


## TODO

- Containerization for deployment online
- Web UI development
- Changing refresh times according to Course Roster (every 10 mins, 20 mins, or 1 hr based on time of day)
