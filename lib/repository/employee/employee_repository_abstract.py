from abc import ABC, abstractmethod

from lib.domain.model.employee import Employee


class EmployeeRepository(ABC):
    @abstractmethod
    def get_by_employee_id(self, employee_id: str) -> Employee:
        pass

    @abstractmethod
    def save(self, employee: Employee):
        pass

    @abstractmethod
    def get_all(self):
        pass
