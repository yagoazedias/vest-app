from abc import ABC, abstractmethod

from domain.model.event import Event

class EmployeeRepository(ABC):
    @abstractmethod
    def get_by_employee_id(self, employee_id: str):
        pass

    @abstractmethod
    def save(self, event: Event):
        pass
