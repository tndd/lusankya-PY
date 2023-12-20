CREATE TABLE IF NOT EXISTS alpaca.bar (
    time_stamp TIMESTAMP WITH TIME ZONE NOT NULL,
    time_frame TEXT NOT NULL,
    symbol TEXT NOT NULL,
    open DOUBLE PRECISION,
    high DOUBLE PRECISION,
    low DOUBLE PRECISION,
    close DOUBLE PRECISION,
    number_of_trades BIGINT,
    volume BIGINT,
    volume_weighted_average_price DOUBLE PRECISION,
    PRIMARY KEY(time_stamp, time_frame, symbol)
);

SELECT create_hypertable('alpaca.bar', 'time_stamp');