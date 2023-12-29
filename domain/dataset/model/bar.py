from dataclasses import dataclass
from datetime import datetime


@dataclass
class Bar:
    t: datetime         # Timestamp
    open: float         # Opening price
    high: float         # High price
    low: float          # Low Price
    close: float        # Closing Price
    volume: int         # Bar volume
    trade_count: int    # Trade count in the bar
    vwap: float         # Volume weighted average price