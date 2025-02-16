from domain.model.event import Event
from usecase.event.event_usecase_abstract import EventUsecase


class VestUsecase(EventUsecase):
    def process(self, event: Event):
        employee = self.employee_repository.get_by_employee_id(event.employee_id)
        if not employee:
            self.employee_repository.save(event)
        elif event.award_id not in employee:
            employee[event.award_id] = {
                "date": event.date,
                "amount": event.amount
            }
        else:
            employee[event.award_id]["amount"] += event.amount