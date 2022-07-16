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

insert into users (category_name) 
values ('Admin');
insert into users (category_name) 
values ('Corretor');
insert into users (category_name) 
values ('Estagiário');

