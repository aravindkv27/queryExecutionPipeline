--liquibase formatted sql

--changeset Aravind:1 labesl:insert queries context:insert
--comment: Inserting a company with all information
INSERT INTO company (name, address1, address2, city) 
VALUES ('Tech Mach', '123 Tech Lane', 'Tech Park Building', 'Tech City');
INSERT INTO company (name) VALUES ('Mind Tree.');

--changeset Aravind:2 labesl:insert queries context:insert status=updated
--comment: Inserting a company with all information
INSERT INTO company (name, address1, address2, city) 
VALUES ('L&t', '123 Tech Lane', 'Tech Park Building', 'Tech City');
