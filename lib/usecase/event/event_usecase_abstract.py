from abc import ABC, abstractmethod

from lib.repository.employee.employee_repository_abstract import EmployeeRepository


class EventUsecase(ABC):
    def __init__(self, repository: EmployeeRepository):
        self.employee_repository = repository

    @abstractmethod
    def process(self, event, target_datetime):
        pass

