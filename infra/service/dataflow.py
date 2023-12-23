from dataclasses import dataclass, field
from uuid import uuid4
from typing import List

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


def regist_api_schedule_list(api_schedules: List[ApiSchedule]):
    """
    実行予定のAPIをリストで登録する
    """
    pass


def regist_api_schedule(api_schedule: ApiSchedule):
    """
    実行予定のAPIを単発で登録する
    """
    regist_api_schedule_list([api_schedule,])


def execute_scheduled_api(api_schedule_id: str):
    """
    実行予定に登録されたAPIをID指定で実行する
    未実行または失敗しているものしか実行しないようにする
    """
    pass


def execute_all_scheduled_api():
    """
    実行予定に登録されているAPIを全て実行する
    """
    pass


def request_api(api_schedule: ApiSchedule):
    """
    渡されたAPI実行情報を即実行し、結果諸共DBへ登録する
    """
    pass


def fetch_successful_api_response_for_endpoint(endpoint: str):
    """
    特定エンドポイントの成功したAPIレスポンスを取得する
    """
    pass


def execute_scheduled_queries():
    """
    実行予定に登録されているクエリを全て実行する
    """
    pass