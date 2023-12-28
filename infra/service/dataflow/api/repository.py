from dataclasses import dataclass
from typing import List

from infra.api.client import ApiSnapshot
from infra.db.psql.client import PsqlClient
from infra.db.sql.helper import Command, Schema, load_query

from .model import ApiRequest, ApiResponse


@dataclass
class ApiFlowRepository:
    cli: PsqlClient

    ### Store ###
    def store_api_request(self, api_request: ApiRequest):
        """
        実行予定のAPIを登録する
        """
        q = load_query(Schema.DATAFLOW, Command.INSERT, 'table_api_request')
        p = api_request.to_params()
        self.cli.execute_queries_with_params(q, p)

    def store_api_response(self, api_response: ApiResponse):
        """
        API実行結果を登録する
        """
        pass

    def store_api_snapshot(self, api_snapshot: ApiSnapshot):
        """
        APIのスナップショットからscheduleとResponseを同時登録する
        """
        pass

    def multi_store_api_requests(self, api_requests: List[ApiRequest]):
        """
        実行予定のAPIを一括で登録する
        """
        pass

    ### Execute ###
    def execute_api(self, api_request_id: str):
        """
        idで指定されたAPIを実行する
        未実行または失敗しているAPIを実行する
        """
        pass

    def multi_execute_api(self):
        """
        未実行または失敗しているAPIを実行する
        """
        pass

    ### Fetch ###
    def fetch_successful_api_response_for_endpoint(self, endpoint: str):
        """
        特定エンドポイントの成功したAPIレスポンスを取得する
        """
        pass