from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ApiResponse:
    api_request_id: str
    status: int
    header: dict
    body: dict
    _id: int = None
    time_stamp: str = field(default_factory=lambda: datetime.now().isoformat())
