from dataclasses import dataclass
from typing import List

from domain.dataset.value import Adjustment, Timeframe

from . import Bar


@dataclass
class BarSet:
    symbol: str
    timeframe: Adjustment
    adjustment: Timeframe
    data: List[Bar]