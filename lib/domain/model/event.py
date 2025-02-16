from datetime import datetime
from abc import ABC, abstractmethod

class Event(ABC):
    def __init__(self, employee_id: str, employee_name: str, award_id: str, date: datetime, amount: int):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.award_id = award_id
        self.date = date
        self.amount = amount

    @abstractmethod
    def to_string(self):
        pass

class VestEvent(Event):
    def to_string(self):
        return f"VestEvent(employee_id={self.employee_id}, employee_name={self.employee_name}, award_id={self.award_id}, date={self.date}, amount={self.amount})"

class CancelEvent(Event):
    def to_string(self):
        return f"CancelEvent(employee_id={self.employee_id}, employee_name={self.employee_name}, award_id={self.award_id}, date={self.date}, amount={self.amount})"