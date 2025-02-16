from repository.employee.employee_repository_abstract import EmployeeRepository
from repository.employee.employee_repository_in_memory import EmployeeRepositoryInMemory

class EmployeeRepositoryFactory:
    @staticmethod
    def create_repository(repository_type: str) -> EmployeeRepository:
        if repository_type == "in_memory":
            return EmployeeRepositoryInMemory()
        else:
            raise ValueError(f"Unexpected repository type {repository_type}")