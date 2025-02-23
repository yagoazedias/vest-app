from lib.repository.employee.employee_repository_factory import EmployeeRepositoryFactory
from lib.usecase.employee.employee_usecase import EmployeeUsecase


class EmployeeUsecaseFactory:
    def __init__(self):
        self.repository = EmployeeRepositoryFactory.create_repository("in_memory")

    def create_usecase(self):
        return EmployeeUsecase(self.repository)