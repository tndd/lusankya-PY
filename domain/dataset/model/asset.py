from dataclasses import dataclass
from typing import Optional


@dataclass
class Asset:
    id_: str
    class_: str
    exchange: str
    symbol: str
    name: str
    status: str
    tradable: bool
    marginable: bool
    shortable: bool
    easy_to_borrow: bool
    fractionable: bool
    maintenance_margin_requirement: Optional[str] = None
    attributes: Optional[list] = None
    min_order_size: Optional[float] = None
    min_trade_increment: Optional[float] = None
    price_increment: Optional[float] = None