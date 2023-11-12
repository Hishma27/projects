show databases;
create database authentication1;
use authentication1;
create table userinfo(fullname varchar(20), username varchar(30), pwd varchar(20));
insert into userinfo values('Hishma','hishma2711@gmail.com','Hishma@123');
select * from userinfo;
