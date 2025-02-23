from lib.domain.model.equity import Equity
from lib.domain.model.event import Event
from lib.domain.model.employee import EmployeeBuilder
from lib.usecase.event.event_usecase_abstract import EventUsecase


class VestUsecase(EventUsecase):
    def process(self, event: Event, target_datetime):
        employee = self.employee_repository.get_by_employee_id(event.employee_id)

        if not employee:
            if event.date <= target_datetime:
                self._save_new_employee_by_event(event)
            else:
                self._save_new_employee_with_zero_amount(event)
        else:
            if event.date <= target_datetime:
                if event.award_id not in employee.equities:
                    self._update_employee_equity_by_event(employee, event)
                else:
                    self._increment_equity_by_event(employee, event)

    def _increment_equity_by_event(self, employee, event):
        employee.equities[event.award_id].amount += event.amount
        self.employee_repository.save(employee)

    def _update_employee_equity_by_event(self, employee, event):
        employee.equities[event.award_id] = Equity(id=event.award_id, amount=event.amount)
        self.employee_repository.save(employee)

    def _save_new_employee_by_event(self, event):
        equity = self._build_equities(event.award_id, event.amount)
        employee = EmployeeBuilder() \
                    .set_id(event.employee_id) \
                    .set_name(event.employee_name) \
                    .set_equities(equity) \
                    .build()
        self.employee_repository.save(employee)

    def _save_new_employee_with_zero_amount(self, event):
        equity = self._build_equities(event.award_id, 0)
        employee = EmployeeBuilder() \
                    .set_id(event.employee_id) \
                    .set_name(event.employee_name) \
                    .set_equities(equity) \
                    .build()
        self.employee_repository.save(employee)

    def _build_equities(self, award_id, amount):
        return {
            award_id: Equity(
                id=award_id,
                amount=amount
            )
        }
