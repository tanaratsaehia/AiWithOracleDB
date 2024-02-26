create table fuel(
    fuel_id number(2) primary key,
    fuel_type varchar2(10) not null
);

create table transmission(
    trans_id number(2) primary key,
    trans_type varchar2(15) not null
);

create table car(
    car_id number(5) primary key,
    model varchar2(150) not null,
    production_year number(4) not null,
    engine_size number(2,1) not null,
    miles_per_gallon number(3,1) not null,
    trans_id number(2) not null,
    fuel_id number(2) not null,
    constraint car_fk_trans foreign key(trans_id) references transmission(trans_id),
    constraint car_fk_fuel foreign key(fuel_id) references fuel(fuel_id)
);

--weak
create table sales_history(
    sale_id number(5) not null,
    user_id number(5) not null,
    status varchar2(20),
    path_picture varchar2(180),
    mile_used number(8) not null,
    predict_price number(6),
    user_offer_price number(6),
    admin_offer_price number(6),
    license_plate varchar2(180) not null,
    car_id number(5) not null,
    constraint sale_pk primary key(sale_id, user_id),
    constraint sh_fk FOREIGN key(car_id) references car(car_id)
);

-- edit --
create table users(
    user_id number(5) primary key,
    user_name varchar2(180) not null,
    password varchar2(256) not null,
    phone_number char(10) not null,
    email varchar2(30),
    address varchar2(250) not null,
    role char(6),
    bank_account_number varchar2(15) not null,
    bank_name varchar2(100) not null
);
-- ex insert
-- insert into users values (1, 'oil', '4c39de83231366548c7756c3ff20f1ad97c1b6c3', '0984321907', null, 'หลังมอ', null, '0984321907', 'กรุงโรม');