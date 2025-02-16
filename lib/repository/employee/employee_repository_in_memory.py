from repository.employee.employee_repository_abstract import EmployeeRepository

class EmployeeRepositoryInMemory(EmployeeRepository):
    def __init__(self):
        self.events = {
            "E001": {
                "name": "Alice Smith",
                "ISO-001": {
                    "date": "2021-01-01",
                    "amount": 1000
                }
            },
            "E002": {
                "name": "Bobby Jones",
                "ISO-001": {
                    "date": "2021-01-01",
                    "amount": 1000
                },
                "NSO-001": {
                    "date": "2021-01-01",
                    "amount": 100
                }
            }
        }

    def get_by_employee_id(self, employee_id: str) -> dict:
        return self.events.get(employee_id)

    def save(self, event):
        self.events[event.employee_id] = event