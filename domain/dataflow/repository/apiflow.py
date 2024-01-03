from concurrent.futures import ProcessPoolExecutor
from dataclasses import dataclass
from typing import List

from domain.dataflow.model import ApiRequest, ApiResponse, ApiResult
from infra.adapter.dataflow import (api_request_to_params,
                                    api_response_to_params,
                                    api_result_to_request_and_response)
from infra.db.client import PsqlClient
from infra.db.sql.loader import Command, Schema, load_query
from infra.service.dataflow import request_api


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
        APIレスポンスを登録する
        """
        query = load_query(Schema.DATAFLOW, Command.INSERT, 'table_api_response')
        param = api_response_to_params(api_response)
        self.cli_db.execute_with_params(query, param)


    def multi_store_api_requests(self, api_requests: List[ApiRequest]):
        """
        実行予定のAPIを一括で登録する
        """
        query = load_query(Schema.DATAFLOW, Command.INSERT, 'table_api_request')
        params_list = [api_request_to_params(a_rq) for a_rq in api_requests]
        self.cli_db.parallel_executemany(query, data=params_list)


    def store_api_result(self, api_result: ApiResult):
        """
        API実行結果を登録する
        """
        # Api実行結果からリクエストとレスポンスを取り出す
        req, res = api_result_to_request_and_response(api_result)
        # リクエストとレスポンスを登録するためのクエリ作成
        req_query = load_query(Schema.DATAFLOW, Command.INSERT, 'table_api_response')
        req_param = api_request_to_params(req)
        res_query = load_query(Schema.DATAFLOW, Command.INSERT, 'table_api_response')
        res_param = api_response_to_params(res)
        # トランザクション処理のためにクエリを纏める
        queries_with_params = [
            (req_query, req_param),
            (res_query, res_param)
        ]
        # 保存
        self.cli_db.execute_queries_with_params(queries_with_params)


    ### Execute ###
    def execute_api(self, api_request_id: str):
        """
        idで指定されたAPIを実行する
        未実行または失敗しているAPIを実行する
        """
        pass

    def execute_api_not_executed_or_failed(self, n_worker: int = 4):
        """
        未実行または失敗しているAPIを実行する
        """
        # APIリクエストの実行と保存を行う並列処理のためのラッパー関数
        def _execute_and_store(rq: ApiRequest):
            api_response = request_api(rq)
            self.store_api_response(api_response)

        # 未実行or失敗リクエストの取得
        api_requests = self.fetch_requests_not_executed_or_failed()
        # 並列処理でAPIを叩く。数を増やしすぎるとリクエスト数の上限を超えてエラーになるので注意。
        with ProcessPoolExecutor(max_workers=n_worker) as executor:
            executor.map(_execute_and_store, api_requests)

    ### Fetch ###
    def fetch_successful_api_response_for_endpoint(self, endpoint: str) -> List[ApiResult]:
        """
        特定エンドポイントの成功かつ未移動のAPIレスポンスを取得する

        Note:
            - これにより得られたレスポンス情報は、datasetドメインに移動されるべきである
            - 返される結果のbodyは巨大である可能性があるため、
                必要な分のみを読み出すための引数にendpointを設けている
        """
        pass

    def fetch_requests_not_executed_or_failed(self) -> List[ApiRequest]:
        """
        全ての未実行あるいは失敗したAPIリクエストのリストを取得する

        これにより取得されるリクエスト情報は、いずれも実行されるべきものである
        """
        pass

    def fetch_requests_not_executed_or_failed_of_endpoint(self, endpoint: str) -> List[ApiRequest]:
        """
        特定エンドポイントの未実行あるいは失敗したAPIリクエストのリストを取得する

        これにより取得されるリクエスト情報は、いずれも実行されるべきものである
        """
        pass