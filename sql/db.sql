create database studentdb;

use studentdb;

create table student(
	srn varchar(256) NOT NULL,
    sname varchar(256) NOT NULL,
    primary key (srn)
);