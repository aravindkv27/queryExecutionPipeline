--liquibase formatted sql

--changeset aravindkv:1 labels:person-table-label context:table-person
--comment: creating a table called person
create table demo12 (
    id int primary key auto_increment not null,
    name varchar(50) not null,
    address1 varchar(50),
    address2 varchar(50),
    city varchar(30)
)


--changeset aravind:2 labels:company-table-label context:create-table-company
--comment: creating table called company
create table school (
    id int primary key auto_increment not null,
    name varchar(50) not null,
    address1 varchar(50),
    address2 varchar(50),
    city varchar(30)
)


--changeset rahul:3 labels:alter-table-column context:add-column
--comment: add column called country in the person table
alter table demo12 add column country varchar(2)


--changeset Aravind:4 labesl:insert queries context:insert
--comment: Inserting a company with all information
INSERT INTO school (name, address1, address2, city) 
VALUES ('Tech Innovators', '123 Tech Lane', 'Tech Park Building', 'Tech City');
INSERT INTO school (name) VALUES ('Global Solutions Inc.');
INSERT INTO school (name, address1, address2, city) 
VALUES ('Creative Designs', '456 Art Avenue', 'Design Plaza', 'Artville');
INSERT INTO school (name) VALUES ('Software Experts Ltd.');
INSERT INTO school (name, address1, address2, city) 
VALUES ('Innovate Solutions', '789 Innovation Street', 'Suite 101', 'Innovation City');




