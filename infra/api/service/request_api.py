from requests import get

from domain.dataflow.model import ApiRequest, ApiResponse
from infra.adapter.dataflow import api_response_from_snapshot
from infra.api.model import ApiSnapshot


def rq_get(endpoint: str, params: dict, header: dict) -> ApiSnapshot:
    """
    通常の形式のリクエスト
    """
    r = get(url=endpoint, params=params, headers=header)
    return ApiSnapshot(
        endpoint,
        params,
        header,
        r.status_code,
        dict(r.headers),
        r.text
    )


def request_api(req: ApiRequest) -> ApiResponse:
    """
    dataflowドメイン形式のリクエストを引数に、同じくdataflowドメイン形式のレスポンスを返す
    """
    api_snapshot = rq_get(endpoint=req.endpoint, params=req.params, header=req.header)
    return api_response_from_snapshot(snapshot=api_snapshot, api_request_id=req._id)
