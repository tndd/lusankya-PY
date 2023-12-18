from dataclasses import dataclass


@dataclass
class ApiResponse:
    id: int
    schedule_id: int
    timestamp: str
    status: int
    header: str
    body: str
