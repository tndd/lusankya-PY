from infra.service.convert_api_response_body import convert_to_query_alpaca_bar


def test_convert_to_query_alpaca_bar():
    mock_body_bar = {
        "bars": [
            {
            "c": 178.21,
            "h": 178.26,
            "l": 178.21,
            "n": 65,
            "o": 178.26,
            "t": "2022-01-03T09:00:00Z",
            "v": 1118,
            "vw": 178.235733
            },
            {
            "c": 178.31,
            "h": 178.34,
            "l": 178.31,
            "n": 26,
            "o": 178.33,
            "t": "2022-01-03T09:02:00Z",
            "v": 1218,
            "vw": 178.331486
            },
            {
            "c": 178.3,
            "h": 178.3,
            "l": 178.28,
            "n": 30,
            "o": 178.28,
            "t": "2022-01-03T09:03:00Z",
            "v": 814,
            "vw": 178.289889
            }
        ],
        "next_page_token": "QUFQTHxNfDE2NDEyMDA1ODAwMDAwMDAwMDA=",
        "symbol": "AAPL"
    }
    expect_query = """INSERT INTO alpaca_bar (time_stamp, time_frame, symbol, open, high, low, close, number_of_trades, volume, volume_weighted_average_price) SELECT (json_data->>'t')::timestamp, 1Min, AAPL, (json_data->>'o')::double precision, (json_data->>'h')::double precision, (json_data->>'l')::double precision, (json_data->>'c')::double precision, (json_data->>'n')::bigint, (json_data->>'v')::bigint, (json_data->>'vw')::double precision FROM json_array_elements('[{"c": 178.21, "h": 178.26, "l": 178.21, "n": 65, "o": 178.26, "t": "2022-01-03T09:00:00Z", "v": 1118, "vw": 178.235733}, {"c": 178.31, "h": 178.34, "l": 178.31, "n": 26, "o": 178.33, "t": "2022-01-03T09:02:00Z", "v": 1218, "vw": 178.331486}, {"c": 178.3, "h": 178.3, "l": 178.28, "n": 30, "o": 178.28, "t": "2022-01-03T09:03:00Z", "v": 814, "vw": 178.289889}]') AS json_data;"""
    assert expect_query == convert_to_query_alpaca_bar(mock_body_bar, '1Min')
