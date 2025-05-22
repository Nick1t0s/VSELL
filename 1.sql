CREATE TABLE IF NOT EXISTS lots(
    id serial PRIMARY KEY,
    model text NOT NULL ,
    used bool NOT NULL ,
    cost int NOT NULL,
    place text,
    statePOD text,
    stateCART text,
    color text,


)