import os
import random

from twilio.rest import Client

ACCOUNT_SID = os.getenv('TWILIO_ACCOUNT_SID')
AUTH_TOKEN = os.getenv('TWILIO_AUTH_TOKEN')
TWILIO_NUMBER = os.getenv('TWILIO_NUMBER')


def send_kitties_update_sms(recipient_number, kitty_statuses):
    sms_message = 'Hey mamacita, here\'s an update from Project Adopt the Kitties:\n\n'
    for kitty_status in kitty_statuses:
        sms_message += __parse_kitty_status_to_sms__(kitty_status)
    __send_sms__(recipient_number, sms_message.strip(' \t\n\r'))


def __send_sms__(recipient_number, message):
    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        body=message,
        from_=TWILIO_NUMBER,
        to=recipient_number,
        media_url=__get_random_image_url__()
    )

    print(f'Message status: {message.status}')
    print(f'Message error: {message.error_message}')


def __parse_kitty_status_to_sms__(kitty_status):
    if kitty_status.is_adopted:
        return f'!{kitty_status.name}\'s status: {kitty_status.outcome_type} | {kitty_status.outcome_subtype} on {kitty_status.date.strftime("%m/%d/%Y %H:%M:%S")}\n\n '
    else:
        return f'{kitty_status.name}\'s status: Hasn\'t changed yet, baby girl\n\n'


def __get_random_image_url__():
    lines = open('./assets/photo_urls').read().splitlines()
    return random.choice(lines)
