USE project;

DELIMITER //
CREATE PROCEDURE addCustomer(IN cust_name char(50), cust_phone int(10), cust_zip varchar(10), cust_address varchar(50))
BEGIN
	insert into customer values(null, cust_name, cust_phone, cust_zip, cust_address, null, null);
END //

DELIMITER ;