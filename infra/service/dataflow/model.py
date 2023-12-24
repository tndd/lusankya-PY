from dataclasses import dataclass, field
from uuid import uuid4


@dataclass
class ApiSchedule:
    endpoint: str
    params: dict
    header: dict
    _id: str = field(default_factory=uuid4)
    time_stamp: str = None


@dataclass
class ApiResponse:
    api_schedule_id: str
    status: int
    header: dict
    body: dict
    _id: int = None
    time_stamp: str = None


@dataclass
class QuerySchedule:
    time_stamp: str
    query: str
    _id: int = None