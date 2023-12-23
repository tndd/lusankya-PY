from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class ApiSchedule:
    _id: str = field(default_factory=uuid4)
    time_stamp: str
    endpoint: str
    params: dict
    header: dict


@dataclass
class ApiResponse:
    _id: int = None
    api_schedule_id: str
    time_stamp: str
    status: int
    header: dict
    body: dict


@dataclass
class QuerySchedule:
    _id: int = None
    time_stamp: str
    query: str