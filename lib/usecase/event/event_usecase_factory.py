from lib.domain.model.event import Event, VestEvent, CancelEvent
from lib.repository.employee.employee_repository_factory import EmployeeRepositoryFactory
from lib.usecase.event.cancel_usecase import CancelUsecase
from lib.usecase.event.vest_usecase import VestUsecase


class EventUsecaseFactory:
    def __init__(self):
        self.repository = EmployeeRepositoryFactory.create_repository("in_memory")

    def create_usecase(self, event: Event):
        if isinstance(event, VestEvent):
            return VestUsecase(self.repository)
        elif isinstance(event, CancelEvent):
            return CancelUsecase(self.repository)
        else:
            raise ValueError(f"Unexpected event type {type(event)}")