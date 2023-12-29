from enum import Enum


class Adjustment(str, Enum):
    RAW: str = "raw"
    SPLIT: str = "split"
    DIVIDEND: str = "dividend"
    ALL: str = "all"