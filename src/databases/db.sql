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
    modified_by text 
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