from .model import ApiSchedule, ApiResponse
from typing import List


def store_api_schedule(api_schedule: ApiSchedule):
    """
    実行予定のAPIを登録する
    """
    pass


def store_api_response(api_response: ApiResponse):
    """
    API実行結果を登録する
    """
    pass


def multi_store_api_schedules(api_schedules: List[ApiSchedule]):
    """
    実行予定のAPIを一括で登録する
    """
    pass


def execute_scheduled_api(api_schedule_id: str):
    """
    実行予定に登録されたAPIをID指定で実行する
    未実行または失敗しているものしか実行しないようにする
    """
    pass


def multi_execute_scheduled_api():
    """
    実行予定に登録されているAPIを全て実行する
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