DROP DATABASE project;
CREATE DATABASE project;
USE project;

CREATE TABLE supplier (
	supplier_id int(11),
    supplier_name varchar(50),
    supplier_phone varchar(11),
    supplier_email varchar(50),
    PRIMARY KEY (supplier_id)
) ENGINE=InnoDB;

CREATE TABLE supplier_invoice (
	invoice_id int(11) auto_increment,
    supplier_id int(11),
    invoice_date date,
    FOREIGN KEY (supplier_id) REFERENCES supplier (supplier_id),
    PRIMARY KEY (invoice_id)
) ENGINE=InnoDB;

CREATE TABLE product (
	product_id int(11),
    supplier_id int(11),
    product_name varchar(50),
    product_cost float,
    product_description varchar(100),
    FOREIGN KEY (supplier_id) REFERENCES supplier (supplier_id),
    PRIMARY KEY (product_id)
) ENGINE=InnoDB;

CREATE TABLE supplier_invoice_line (
	line_number int(11),
    invoice_id int(11),
    product_id int(11),
    line_quantity int(10),
    FOREIGN KEY (invoice_id) REFERENCES supplier_invoice (invoice_id),
    FOREIGN KEY (product_id) REFERENCES product (product_id),
    PRIMARY KEY (line_number, invoice_id)
) ENGINE=InnoDB;

CREATE TABLE customer (
	customer_id int(11) auto_increment,
    customer_name char(50),
    customer_phone varchar(10),
    customer_zip varchar(10),
    customer_address varchar(50),
    customer_lastService date,
    customer_appointmentReminders int(3),
    PRIMARY KEY (customer_id)
) ENGINE=InnoDB;

CREATE TABLE employee (
	employee_id int(11) auto_increment,
    employee_name char(50),
    employee_phone varchar(10),
    employee_zip varchar(10),
    employee_address varchar(50),
    employee_hourly_pay float,
    employee_startDate date,
    employee_endDate date,
    PRIMARY KEY (employee_id)
) ENGINE=InnoDB;

CREATE TABLE service (
	service_id int(11),
    service_name varchar(20),
    service_price float,
    PRIMARY KEY (service_id)
) ENGINE=InnoDB;

CREATE TABLE customer_invoice (
	invoice_id int(11) auto_increment,
    customer_id int(11),
    employee_id int(11),
    invoice_date date,
    invoice_total float,
    invoice_balance float,
    invoice_billed date,
    PRIMARY KEY (invoice_id)
) ENGINE=InnoDB;

CREATE TABLE customer_invoice_line (
	line_number int(11),
    invoice_id int(11),
    product_id int(11),
    service_id int(11),
    line_type char(11),
    line_quantity int(11),
    FOREIGN KEY (invoice_id) REFERENCES customer_invoice (invoice_id),
    FOREIGN KEY (product_id) REFERENCES product (product_id),
    FOREIGN KEY (service_id) REFERENCES service (service_id),
    PRIMARY KEY (line_number, invoice_id)
) ENGINE=InnoDB;

CREATE TABLE appointment (
	appointment_id int(11) auto_increment,
    customer_id int(11),
    employee_id int(11),
    appointment_description varchar(100),
    appointment_date datetime,
    FOREIGN KEY (customer_id) REFERENCES customer (customer_id),
    FOREIGN KEY (employee_id) REFERENCES employee (employee_id),
    PRIMARY KEY (appointment_id)
) ENGINE=InnoDB;

CREATE TABLE inventory (
	employee_id int(11),
    product_id int(11),
    inventory_quantity int(11),
    FOREIGN KEY (employee_id) REFERENCES employee (employee_id),
    FOREIGN KEY (product_id) REFERENCES product (product_id),
    PRIMARY KEY (employee_id, product_id)
) ENGINE=InnoDB;

CREATE TABLE payment (
	payment_id int(11),
    invoice_id int(11),
    payment_amount float,
    payment_date datetime,
    FOREIGN KEY (invoice_id) REFERENCES customer_invoice(invoice_id),
    PRIMARY KEY (payment_id)
) ENGINE=InnoDB;