CREATE TABLE IF NOT EXISTS lots(
    id serial PRIMARY KEY,
    created timestamp DEFAULT now() NOT NULL,
    model text NOT NULL,
    description text,
    used bool NOT NULL,
    cost int NOT NULL,
    place text,

    condPOD text,
    condCART text,
    color text,

    puffs int,

    taste text,

    evap bool,
    evapR int,
    condEvap text,

    stocks text
)