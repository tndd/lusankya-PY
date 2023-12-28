from infra.api.client import ApiSnapshot
from .model import ApiRequest, ApiResponse
from typing import Tuple


def snapshot_to_schedule(snapshot: ApiSnapshot) -> ApiRequest:
    return ApiRequest(
        endpoint=snapshot.endpoint,
        params=snapshot.query,
        header=snapshot.header
    )


def snapshot_to_response(snapshot: ApiSnapshot, api_request_id: str) -> ApiResponse:
    return ApiResponse(
        api_request_id=api_request_id,
        status=snapshot.r_status,
        header=snapshot.r_header,
        body=snapshot.r_body
    )


def snapshot_to_schedule_and_response(
        snapshot: ApiSnapshot
    ) -> Tuple[ApiRequest, ApiResponse]:
    api_request = ApiRequest(
        endpoint=snapshot.endpoint,
        params=snapshot.query,
        header=snapshot.header
    )
    api_response = ApiResponse(
        api_request_id=api_request._id,
        status=snapshot.r_status,
        header=snapshot.r_header,
        body=snapshot.r_body
    )
    return api_request, api_response
