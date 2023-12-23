CREATE TABLE IF NOT EXISTS dataflow.query_schedule (
	id serial NOT NULL,
	time_stamp timestamptz NOT NULL DEFAULT now(),
	query text NOT NULL,
	CONSTRAINT query_schedule_pkey PRIMARY KEY (id)
);