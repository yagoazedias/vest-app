from domain.model.event import Event
from usecase.event.event_usecase_abstract import EventUsecase


class CancelUsecase(EventUsecase):
    def process(self, event: Event):
        self.employee_repository.save(event)