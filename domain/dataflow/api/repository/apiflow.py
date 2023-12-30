from dataclasses import dataclass
from typing import List

from infra.db.client import PsqlClient
from infra.db.sql.helper import Command, Schema, load_query

from ..model import ApiRequest, ApiResponse


@dataclass
class ApiFlowRepository:
    cli_db: PsqlClient

    ### Store ###
    def store_api_request(self, api_request: ApiRequest):
        """
        実行予定のAPIを登録する
        """
        self.multi_store_api_requests([api_request,])

    def store_api_response(self, api_response: ApiResponse):
        """
        API実行結果を登録する
        """
        pass

    def store_api_req_res(self, api_request: ApiRequest, api_response: ApiResponse):
        """
        APIのRequestとResponseを同時登録する
        """
        pass

    def multi_store_api_requests(self, api_requests: List[ApiRequest]):
        """
        実行予定のAPIを一括で登録する
        """
        q = load_query(Schema.DATAFLOW, Command.INSERT, 'table_api_request')
        params = [ar.to_params() for ar in api_requests]
        self.cli_db.parallel_executemany(q, data=params)

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