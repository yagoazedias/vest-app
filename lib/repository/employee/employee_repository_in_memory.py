from typing import Optional

from lib.domain.model.employee import Employee
from lib.repository.employee.employee_repository_abstract import EmployeeRepository
from lib.repository.state import state


class EmployeeRepositoryInMemory(EmployeeRepository):
    def get_all(self):
        return state.employees

    def get_by_employee_id(self, employee_id: str) -> Optional[Employee]:
        employee = state.employees.get(employee_id)
        if employee is None:
            return None
        return Employee.from_dict(employee)


    def save(self, employee: Employee):
        employee_dict = employee.to_dict()
        state.employees[employee.id] = employee_dict