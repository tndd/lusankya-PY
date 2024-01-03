from typing import Tuple

from domain.dataflow.model import ApiRequest, ApiResponse, ApiResult
from infra.api.model import ApiSnapshot


def api_result_from_snapshot(
        snapshot: ApiSnapshot
    ) -> ApiResult:
    return ApiResult(
        endpoint=snapshot.endpoint,
        params=snapshot.query,
        header=snapshot.header,
        r_status=snapshot.r_status,
        r_header=snapshot.r_header,
        r_body=snapshot.r_body
    )


def api_result_to_request_and_response(
        result: ApiResult
    ) -> Tuple[ApiRequest, ApiResponse]:
    api_request = ApiRequest(
        endpoint=result.endpoint,
        params=result.params,
        header=result.header,
        _id=result._id,
        time_stamp=result.time_stamp
    )
    api_response = ApiResponse(
        api_request_id=result._id,
        status=result.r_status,
        header=result.r_header,
        body=result.r_body,
        time_stamp=result.time_stamp
    )
    return api_request, api_response
