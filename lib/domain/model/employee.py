from dataclasses import dataclass
from typing import Dict

from lib.domain.model.equity import Equity

@dataclass
class Employee:
    id: str
    name: str
    equities: Dict[str, Equity]