from dataclasses import dataclass


@dataclass
class ApiSchedule:
    id: int
    datetime: str
    endpoint: str
    params: dict
    header: dict
