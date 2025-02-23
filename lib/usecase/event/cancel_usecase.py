from lib.domain.model.event import Event
from lib.usecase.event.event_usecase_abstract import EventUsecase


class CancelUsecase(EventUsecase):
    def process(self, event: Event, target_datetime):
        pass