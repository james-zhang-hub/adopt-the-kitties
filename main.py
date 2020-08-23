import kitty_status_service
from austin_animal_data_service import get_animal_outcome_data
from sms_service import send_kitties_update_sms

KITTY_IDS = {'A821879': 'Jackson',
             'A821878': 'Betty'}
RECIPIENT_NUMBERS = ['+12145572892']
# RECIPIENT_NUMBERS = ['+16236806997', '+12145572892']

animal_outcomes = get_animal_outcome_data()

kitty_statuses = []
for kitty_id, kitty_name in KITTY_IDS.items():
    kitty_statuses.append(kitty_status_service.get_kitty_status(kitty_id, kitty_name, animal_outcomes))

for recipient_number in RECIPIENT_NUMBERS:
    send_kitties_update_sms(recipient_number, kitty_statuses)
