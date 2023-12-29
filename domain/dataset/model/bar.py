from dataclasses import dataclass
from datetime import datetime
from typing import List

from domain.dataset.value import Adjustment, Timeframe


@dataclass
class Bar:
    t: datetime             # Timestamp
    open: float             # Opening price
    high: float             # High price
    low: float              # Low Price
    close: float            # Closing Price
    volume: int             # Bar volume
    trade_count: int        # Trade count in the bar
    vwap: float             # Volume weighted average price


@dataclass
class BarSet:
    symbol: str
    timeframe: Adjustment
    adjustment: Timeframe
    data: List[Bar]