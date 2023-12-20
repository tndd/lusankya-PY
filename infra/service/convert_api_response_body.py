import json

def convert_to_query_alpaca_bar(body: dict, timeframe: str) -> str:
    query =  f"""
        INSERT INTO alpaca_bar (time_stamp, time_frame, symbol, open, high, low, close, number_of_trades, volume, volume_weighted_average_price)
        SELECT 
            (json_data->>'t')::timestamp, 
            {timeframe}, 
            {body['symbol']}, 
            (json_data->>'o')::double precision, 
            (json_data->>'h')::double precision, 
            (json_data->>'l')::double precision, 
            (json_data->>'c')::double precision, 
            (json_data->>'n')::bigint, 
            (json_data->>'v')::bigint, 
            (json_data->>'vw')::double precision
        FROM json_array_elements('{json.dumps(body['bars'])}') AS json_data;
    """
    return ' '.join(query.split())