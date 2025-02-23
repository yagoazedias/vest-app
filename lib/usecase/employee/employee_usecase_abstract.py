from abc import ABC, abstractmethod
from lib.repository.employee.employee_repository_abstract import EmployeeRepository


class EmployeeUsecase(ABC):
    def __init__(self, repository: EmployeeRepository):
        self.repository = repository

    @abstractmethod
    def get_all(self):
        pass