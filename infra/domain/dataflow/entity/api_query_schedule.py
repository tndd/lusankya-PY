from dataclasses import dataclass


@dataclass
class ApiQuerySchedule:
    api_schedule_id: int
    timestamp: str
    query: str
