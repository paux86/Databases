USE project;
drop procedure updateEmployee;

DELIMITER //
CREATE PROCEDURE updateEmployee(IN emp_id int, emp_name char(50), emp_phone int, emp_zip varchar(50), emp_address varchar(50), emp_hrlypay float, emp_start date, emp_end date)
BEGIN
	update employee
    set employee_name = emp_name, employee_phone = emp_phone, employee_zip = emp_zip, employee_address = emp_address, employee_hourly_pay = emp_hrlypay, employee_startDate = emp_start, employee_endDate = emp_end
    where employee_id = emp_id;
END //

DELIMITER ;