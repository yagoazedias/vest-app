from dataclasses import dataclass
from typing import Dict

from lib.domain.model.equity import Equity

@dataclass
class Employee:
    id: str
    name: str
    equities: Dict[str, Equity]

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "equities": {k: v.to_dict() for k, v in self.equities.items()}
        }

    @staticmethod
    def from_dict(data: dict):
        equities = {
            equity_id: Equity(
                id=equity_id,
                amount=equity_data["amount"]
            )
            for equity_id, equity_data in data.get("equities", {}).items()
        }

        employee = EmployeeBuilder() \
            .set_id(data["id"]) \
            .set_name(data["name"]) \
            .set_equities(equities) \
            .build()

        return employee


class EmployeeBuilder:
    def __init__(self):
        self._id = None
        self._name = None
        self._equities = None

    def set_id(self, id: str):
        self._id = id
        return self

    def set_name(self, name: str):
        self._name = name
        return self

    def set_equities(self, equities: [Equity]):
        self._equities = equities
        return self

    def build(self):
        return Employee(
            id=self._id,
            name=self._name,
            equities=self._equities
        )

