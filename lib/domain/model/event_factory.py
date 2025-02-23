from datetime import datetime

from lib.constants.events import EVENT_DATE_FORMAT, EVENT_CANCEL_TYPE, EVENT_VEST_TYPE
from lib.domain.model.event import VestEvent, CancelEvent

class EventFactory:
    @staticmethod
    def create(event_type: str, employee_id: str, employee_name, award_id, date: str, amount: str):
        event_date = datetime.strptime(date, EVENT_DATE_FORMAT)
        amount = int(amount)

        if event_type == EVENT_VEST_TYPE:
            return VestEvent(employee_id, employee_name, award_id, event_date, amount)
        elif event_type == EVENT_CANCEL_TYPE:
            return CancelEvent(employee_id, employee_name, award_id, event_date, amount)
        else:
            raise ValueError(f"Unexpected event type {event_type}")
