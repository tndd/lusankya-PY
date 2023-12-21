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
    header: dict
    body: dict


@dataclass
class ApiQuerySchedule:
    api_schedule_id: int
    timestamp: str
    query: str


def regist_api_schedule(endpoint: str, params: dict, header: dict):
    """
    Record and schedule all the necessary information for api execution.
    """
    pass


def execute_scheduled_api(api_schedule_id: str):
    """
    Executes the api of the specified id.
    If it is one that has not been executed or has failed.
    """
    pass


def execute_scheduled_queries():
    """
    Execute all scheduled queries.
    For queries that have been successfully executed, they are deleted.
    """
    pass