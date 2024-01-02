from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class ApiResult:
    endpoint: str
    params: dict
    header: dict
    r_status: int
    r_header: dict
    r_body: dict
    _id: str = field(default_factory=uuid4)
    time_stamp: str = field(default_factory=lambda: datetime.now().isoformat())