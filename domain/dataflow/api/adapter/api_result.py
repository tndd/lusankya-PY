from typing import Tuple

from domain.dataflow.api.model import ApiRequest, ApiResponse, ApiResult
from infra.api.interface import ApiSnapshot


def snapshot_result(
        snapshot: ApiSnapshot
    ) -> ApiResult:
    return ApiResult(
        endpoint=snapshot.endpoint,
        params=snapshot.query,
        header=snapshot.header,
        r_status=snapshot.status,
        r_header=snapshot.header,
        r_body=snapshot.body
    )


def result_to_request_and_response(
        result: ApiRequest
    ) -> Tuple[ApiRequest, ApiResponse]:
    api_request = ApiRequest(
        endpoint=result.endpoint,
        params=result.params,
        header=result.header,
        _id=result._id,
        time_stamp=result.time_stamp
    )
    api_response = ApiResponse(
        api_request_id=result._id._id,
        status=result.r_status,
        header=result.r_header,
        body=result.r_body,
        time_stamp=result.time_stamp
    )
    return api_request, api_response
