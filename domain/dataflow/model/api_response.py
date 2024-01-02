from dataclasses import dataclass, field
from datetime import datetime
from uuid import uuid4


@dataclass
class ApiResponse:
    api_request_id: str
    status: int
    header: dict
    body: str
    _id: str = field(default_factory=lambda: str(uuid4()))
    time_stamp: str = field(default_factory=lambda: datetime.now().isoformat())
