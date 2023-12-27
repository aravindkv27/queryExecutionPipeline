--liquibase formatted sql

--changeset aravindkv:1 labels:person-table-label context:table-person
--comment: creating a table called person
create table company (
    id int primary key auto_increment not null,
    name varchar(50) not null,
    address1 varchar(50),
    address2 varchar(50),
    city varchar(30)
)
--rollback DROP TABLE person;