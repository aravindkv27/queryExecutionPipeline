--liquibase formatted sql


--changeset demo:1 labses:create_table context:table
--comment: table creation
create demo1.test3 (
	id int primary key,
	firstname varchar(50),
	lastname varchar(50) not null,

);
--rollback DROP TABLE demo1.test3;
