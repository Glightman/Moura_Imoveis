CREATE TABLE users(
    id serial PRIMARY KEY,
    name VARCHAR(60) NOT NULL,
    birthday DATE NOT NULL,
    password VARCHAR(10) NOT NULL,
    role VARCHAR(25) NOT NULL,
    email VARCHAR(120) NOT NULL,
    phone_number VARCHAR(25) NOT NULL
);

insert into users (name, birthday, password, role, email, phone_number) 
values ('Gabriel Santana', '07/08/1997', 'Kaga@2019', 'Admin', 'rezbosa@gmail.com', '73988931076');

CREATE TABLE category(
    id serial PRIMARY KEY,
    category_name VARCHAR(60) NOT NULL
);

insert into img_user (user_id, img_url)
values (2, 'https://lh3.googleusercontent.com/Occzoo2LNM_
iedcllpD1TlI2ag667HoMmvAxD41XZNkznD8lQXJr3NiVOqlO5mFOqp66DWAfkori_
8FVaBp1D9ZUdYUxkyyq19d-D7ftTV0zPJKiytCAovxSbA7-jhbBkzcfiJUYkjtIGb2mG
95KM87ihw1esvA84nBllEKS7g0s3azNDN4bTP35aD2Vcpn1eLM5pJtduW-gi09TQ2YUjk
gVqkrECzUevbusFwVzehcrknme3HmR7eqUmTLLEgccbOUON3nwC1fiTrtRYqEglEwQHOE
oLNEmK63tWHEk2xA2GfBcClOFk6KvFUynGHz7mq9-tYKoYP5fQ7Nantz0wsG6ysYsqVB
E0XZTHg-eXDOwPvbmO17aSk1pWH1SOlv5kMR_gWGRNtN2CyOqVMVxTPEWtBlM-tEXa_E_
3pHEuERSX_yGN8fBsqtruV2p715WtPG3-zhE-gb76Kf_TPZiSNcgIXkhH-B2DnpxxdPf
RPNRiATuSnHW_ZVJ7xyWQ-KhZ6DUXCAcpeqiXNHRmgquilqemtYYxwuBTrw-agW6MZVY-
LYCrlN_SrNf3lddGffQwqmelfXnXoOEf1rev7VZ9ekOcotnaD1vVPiitYP2eoGO2_WJrt
EPshNGWcr_kin8LAspvcnMdhcTEC5FoGECe_Q26-aYA5AaftY93c5mirohSFvmebSU1kb
aOlNpVPa17Cc5pBzDSMubYWlzf2J1ZTcnkTEgTnn9IaL38AFrGP003e1jg9DJR94U7ow=w
1348-h903-no?authuser=0')

insert into imovel (user_id, status_id, category_id, prop_state_id,
space_id_id, banheiro, quarto, cidade, bairro, views, data_cadastro,
price)
values (2, 1, 3, 2, 1, 2, 3, 'Porto Seguro', 'Village II', 0,
'07/17/2022', 365000);

insert into users (name, birthday, password, role, email, phone_number) 
values ('Victor Moura', '01/12/1999', 'regina1962', 'Corretor imobiliário', 
'vitors-dm@hotmail.com', '73991172026');

insert into users (category_name) 
values ('Admin');
insert into users (category_name) 
values ('Corretor');
insert into users (category_name) 
values ('Estagiário');

insert into imovel (user_id, status_id, category_id,
prop_state_id, space_id, banheiro, quarto, cidade,
visualizacoes, data_cadastro, price)
values (2, );










create table users(
id serial primary key,
name varchar(60) not null,
birthday date not null,
password varchar(10) not null,
role varchar(25) not null,
email varchar(120) not null,
phone_number varchar(25));

insert into users (name, birthday, password, role, email, phone_number) 
values ('Gabriel Santana', '07/08/1997', 'Kaga@2019', 'Admin', 'gabriellima36716@gmail.com', '73988931076');

insert into users (name, birthday, password, role, email, phone_number) 
values ('Victor Moura', '01/12/1999', 'regina1962', 'Corretor imobiliário', 
'vitors-dm@hotmail.com', '73991172026');

create table imovel(
id serial primary key,
user_id int references users(id) not null,
status varchar(60) not null,
category varchar(60) not null,
prop_state varchar(60) not null,
space varchar(250) not null,
banheiros int not null,
quartos int not null,
cidade varchar(25) not null,
bairro varchar(25) not null,
views int not null,
data_cadastro date not null,
price money not null,
rua varchar(120) not null,
area int not null);

insert into imovel (user_id, status, category, prop_state, space, banheiros, quartos, cidade, bairro, views, data_cadastro, price, rua, area)
values (2, 'para vender', 'casa', 'mobiliada', 'piscina, garagem, area de churrasco', 3, 3, 'Porto Seguro', 'Vilage II', 0, '07/19/2022', 680000, 'rua das gromélias', 400)

create table img_imovel(
id serial primary key,
imovel_id int references imovel(id) not null,
img_url varchar(1000) not null);

create table img_user(
id serial primary key,
user_id int references users(id) not null,
img_url varchar(1000) not null);

