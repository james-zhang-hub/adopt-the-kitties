from dateutil.parser import parse


class KittyStatus:
    def __init__(self, kitty_name, kitty_status_data=None, is_adopted=False):
        if is_adopted:
            self.name = kitty_name
            self.id = kitty_status_data['animal_id']
            self.outcome_type = kitty_status_data['outcome_type']
            self.date = parse(kitty_status_data['datetime'])
            self.outcome_subtype = kitty_status_data['outcome_subtype']
            self.is_adopted = is_adopted
        else:
            self.name = kitty_name
            self.is_adopted = is_adopted


def get_kitty_status(kitty_id, kitty_name, data):
    try:
        kitty_status_data = next(status for status in data if status['animal_id'] == kitty_id)
        return KittyStatus(kitty_name, kitty_status_data, True)

    except StopIteration:
        return KittyStatus(kitty_name)
