from dataclasses import dataclass
from datetime import datetime
from typing import List


@dataclass
class Bar:
    t: datetime  # Timestamp
    o: float     # Opening price
    h: float     # High price
    l: float     # Low Price
    c: float     # Closing Price
    v: int       # Bar volume
    n: int       # Trade count in the bar
    vw: float    # Volume weighted average price


@dataclass
class SymbolBars:
    symbol: str
    data: List[Bar]
