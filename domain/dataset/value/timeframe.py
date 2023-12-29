from enum import Enum


class TimeFrame(str, Enum):
    MIN: str = "1Min"
    MIN_5: str = "5Min"
    MIN_15: str = "15Min"
    HOUR: str = "1Hour"
    DAY: str = "1Day"
    WEEK: str = "1Week"
    MONTH: str = "1Month"