--liquibase formatted sql

--changeset aravindkv:1 labels:person-table-label context:table-person
--comment: creating a table called person
create table person (
    id int primary key auto_increment not null,
    name varchar(50) not null,
    address1 varchar(50),
    address2 varchar(50),
    city varchar(30)
)
--rollback DROP TABLE person;

--changeset aravind:2 labels:company-table-label context:create-table-company
--comment: creating table called company
create table company (
    id int primary key auto_increment not null,
    name varchar(50) not null,
    address1 varchar(50),
    address2 varchar(50),
    city varchar(30)
)
--rollback DROP TABLE company;

--changeset rahul:3 labels:alter-table-column context:add-column
--comment: add column called country in the person table
alter table person add column country varchar(2)
--rollback ALTER TABLE person DROP COLUMN country;

--changeset Aravind:4 labesl:insert queries context:insert
--comment: Inserting a company with all information
INSERT INTO company (name, address1, address2, city) 
VALUES ('Tech Innovators', '123 Tech Lane', 'Tech Park Building', 'Tech City');
INSERT INTO company (name) VALUES ('Global Solutions Inc.');
INSERT INTO company (name, address1, address2, city) 
VALUES ('Creative Designs', '456 Art Avenue', 'Design Plaza', 'Artville');
INSERT INTO company (name) VALUES ('Software Experts Ltd.');
INSERT INTO company (name, address1, address2, city) 
VALUES ('Innovate Solutions', '789 Innovation Street', 'Suite 101', 'Innovation City');
--rollback DELETE FROM company WHERE name IN ('Tech Innovators','Global Solutions Inc.','Creative Designs','Software Experts Ltd.','Innovate Solutions');
--rollback ALTER TABLE company AUTO_INCREMENT = 1;  



