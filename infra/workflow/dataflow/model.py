from dataclasses import dataclass


@dataclass
class ApiSchedule:
    id: int
    datetime: str
    endpoint: str
    params: dict
    header: dict


@dataclass
class ApiResponse:
    id: int
    schedule_id: int
    timestamp: str
    status: int
    header: str
    body: str


@dataclass
class ApiQuerySchedule:
    api_schedule_id: int
    timestamp: str
    query: str
