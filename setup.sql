
CREATE DATABASE CONTACT_DB;
CREATE TABLE CONTACT_DB.Persons ( PersonID int NOT NULL AUTO_INCREMENT, fisrtname VARCHAR(20), lastname VARCHAR(20),  PRIMARY KEY (PersonID));
CREATE TABLE CONTACT_DB.Groups ( GroupID int NOT NULL AUTO_INCREMENT, groupname VARCHAR(40) ,  PRIMARY KEY (GroupID,groupname));
CREATE TABLE CONTACT_DB.person_group (PersonID int NOT NULL, GroupID int NOT NULL, FOREIGN KEY (PersonID) REFERENCES Persons(PersonID) ON DELETE CASCADE, FOREIGN KEY (GroupID) REFERENCES Groups(GroupID) ON DELETE CASCADE, PRIMARY KEY (PersonID, GroupID));
CREATE TABLE CONTACT_DB.person_address ( StreetADD varchar(100) NOT NULL, PersonID int NOT NULL, FOREIGN KEY (PersonID) REFERENCES Persons(PersonID) ON DELETE CASCADE, PRIMARY KEY (PersonID, StreetADD));
CREATE TABLE CONTACT_DB.person_email ( emailid varchar(50) NOT NULL, PersonID int NOT NULL, FOREIGN KEY (PersonID) REFERENCES Persons(PersonID) ON DELETE CASCADE , PRIMARY KEY (PersonID, emailid));
CREATE TABLE CONTACT_DB.person_phone ( phoneNUM varchar(15) NOT NULL, PersonID int NOT NULL, FOREIGN KEY (PersonID) REFERENCES Persons(PersonID) ON DELETE CASCADE, PRIMARY KEY (PersonID, phoneNUM) );

CREATE DATABASE public
CREATE TABLE user_rec (userid varchar(50),password varchar(20), primary key(userid,password));
INSERT INTO public.user_rec values('admin','password');