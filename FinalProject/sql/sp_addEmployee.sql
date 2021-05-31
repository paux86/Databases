USE project;

DELIMITER //
CREATE PROCEDURE addEmployee(IN emp_name char(50), emp_phone int(10), emp_zip varchar(10), emp_address varchar(50), emp_rate float, emp_start date)
BEGIN
	insert into employee values(null, emp_name, emp_phone, emp_zip, emp_address, emp_rate, emp_start, null);
END //

DELIMITER ;