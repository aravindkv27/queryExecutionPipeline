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

--changeset aravindkv:1.1 labels:person-table-values context:table-values
--comment: inserting values
INSERT INTO person (name) VALUES ('John Doe');
INSERT INTO person (name, address1, address2, city) VALUES ('Jane Smith', '123 Main St', 'Apt 4B', 'Cityville');
INSERT INTO person (name, city) VALUES ('Alice Johnson', 'Townsville');
INSERT INTO person (name, address1, address2, city) VALUES ('Bob Anderson', '456 Oak St', 'Suite 101', 'Villagetown');
INSERT INTO person (name, city) VALUES ('Eva Brown', 'Hamletsville');
--rollback DELETE FROM person WHERE name IN ('John Doe','Jane Smith','Alice Johnson','Bob Anderson','Eva Brown');
--rollback ALTER TABLE person AUTO_INCREMENT = 1;  

--changeset aravindkv:1.2 labels:person-values context:adding-new-values
--comment: Inserting data for the 'person' table
INSERT INTO person (name, address1, address2, city) VALUES ('Michael Johnson', '123 Main St', 'Apt 101', 'New York');
INSERT INTO person (name, address1, address2, city) VALUES ('Sophia Anderson', '456 Elm St', NULL, 'Los Angeles');
INSERT INTO person (name, address1, address2, city) VALUES ('William Garcia', '789 Oak St', 'Suite 201', 'Chicago');
INSERT INTO person (name, address1, address2, city) VALUES ('Olivia Martinez', '321 Pine St', NULL, 'San Francisco');
INSERT INTO person (name, address1, address2, city) VALUES ('James Rodriguez', '555 Cedar St', 'Unit B', 'Seattle');
--rollback DELETE FROM person WHERE name IN ('Michael Johnson','Sophia Anderson','William Garcia','Olivia Martinez','James Rodriguez');

