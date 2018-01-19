# coursemonitor

This Python 2 module monitors the status of Cornell classes based on the Course Roster, and can
send a SMS via Twilio to your phone when a class is detected as open.

## Installation

- Run `pip install -r requirements.txt` to install the required dependencies for this package.
- Edit `.env_template` with your own values for Twilio, and run `source .env_template` from your terminal for Twilio setup.

If you've never used Twilio before, [check out this link](https://www.twilio.com/docs/quickstart/python/sms#sign-up-for-twilio-and-get-a-phone-number) to get set up.
A free trial should provide sufficient free credit (about $15 worth) for monitoring (text messages cost less than 1 cent).


## TODO

- Web UI development
- Actual UI interaction
- Containerization for deployment online
- Changing refresh times according to Course Roster (every 10 mins, 20 mins, or 1 hr based on time of day)
