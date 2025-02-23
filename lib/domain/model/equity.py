from dataclasses import dataclass

@dataclass
class Equity:
    id: str
    amount: int

    def to_dict(self):
        return {
            "id": self.id,
            "amount": self.amount
        }

    @staticmethod
    def from_dict(data: dict):
        return Equity(
            id=data["id"],
            amount=data["amount"]
        )
