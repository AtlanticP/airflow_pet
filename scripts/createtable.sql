-- Функция, которая создает пользователя, если его не существует
DROP FUNCTION IF EXISTS create_user(name, text);
CREATE OR REPLACE FUNCTION create_user(rname NAME, rpass TEXT) RETURNS void AS
$$
BEGIN 
    IF NOT EXISTS (
		SELECT rolname FROM pg_catalog.pg_roles WHERE rolname = rname
    ) 
    	THEN
	         EXECUTE format('CREATE USER %I WITH PASSWORD %L', rname, rpass);
    END IF;
END
$$
LANGUAGE plpgsql;
SELECT create_user('user1', :pass);

-- создать таблицу Request
DROP TABLE IF EXISTS request;
CREATE TABLE request (
	id					SERIAL PRIMARY KEY,
	"name"				TEXT NOT NULL,
	sex					CHAR NOT NULL,
	applying			timestamp NOT NULL,
    birthday			date NOT NULL,
	region				TEXT,
	children 			INT,
	job					TEXT,
	phone				CHAR(12),
	loan				TEXT,
	loan_size			TEXT,
	residence_type 		CHAR,
	salary				INT,
	CONSTRAINT unique_person UNIQUE ("name", applying, birthday)
);

-- Дать пользователю соответсвующие привелегии (CRUD)
GRANT SELECT, INSERT, UPDATE, DELETE ON TABLE request TO user1;
GRANT USAGE, SELECT ON SEQUENCE request_id_seq TO user1;
