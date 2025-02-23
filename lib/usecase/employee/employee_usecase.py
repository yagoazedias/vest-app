from lib.repository.employee.employee_repository_abstract import EmployeeRepository


class EmployeeUsecase:
    def __init__(self, repository: EmployeeRepository):
        self.employee_repository = repository

    def get_all(self):
        return self.employee_repository.get_all()