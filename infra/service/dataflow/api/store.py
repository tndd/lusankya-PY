from .model import ApiRequest, ApiResponse
from .adapter import snapshot_to_schedule, snapshot_to_response
from typing import List
from infra.api.client import ApiSnapshot


def store_api_request(api_request: ApiRequest):
    """
    実行予定のAPIを登録する
    """
    pass


def store_api_response(api_response: ApiResponse):
    """
    API実行結果を登録する
    """
    pass


def store_api_snapshot(api_snapshot: ApiSnapshot):
    """
    APIのスナップショットからscheduleとResponseを同時登録する
    """
    pass


def multi_store_api_requests(api_requests: List[ApiRequest]):
    """
    実行予定のAPIを一括で登録する
    """
    pass
