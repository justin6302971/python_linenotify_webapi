CREATE SCHEMA notification
    AUTHORIZATION tempuser_local;




CREATE TABLE notification.user_token
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 ),
    target_name text,
    access_token text,
    status boolean,
    created_dt timestamp without time zone  NOT NULL,
    created_by text NOT NULL,
    modified_dt timestamp without time zone,
    modified_by text, 
    PRIMARY KEY (id)
);


ALTER TABLE IF EXISTS notification.user_token
    OWNER to tempuser_local;


CREATE TABLE notification."user"
(
    id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 ),
    name text NOT NULL,
    email text NOT NULL,
    password text NOT NULL,
    status boolean,
    created_dt timestamp without time zone NOT NULL,
    created_by text NOT NULL,
    modified_dt timestamp without time zone,
    modified_by text,
    PRIMARY KEY (id)
);

ALTER TABLE IF EXISTS notification."user"
    OWNER to tempuser_local;




-- temporary script 
-- INSERT INTO notification."user"(name, email, password, created_dt, created_by, status)
-- 	VALUES ('justin', 'justin6302971@gmail.com', 'pbkdf2:sha256:260000$phLd8Rh2mj9Nsp56$711efa29749a154815999f2fbc7012544888ba4a8a6f314a576d6f6221b7a353', '2022-12-06 12:33:20.424968','system', True);