USE project;
-- drop procedure updateCustomer;

DELIMITER //
CREATE PROCEDURE updateCustomer(IN cus_id int, cus_name char(50), cus_phone int, cus_zip varchar(50), cus_address varchar(50), cus_lastService date, cus_apptReminders int)
BEGIN
	update customer
    set customer_name = cus_name, customer_phone = cus_phone, customer_zip = cus_zip, customer_address = cus_address, customer_lastService = cus_lastService, customer_appointmentReminders = cus_apptReminders
    where customer_id = cus_id;
END //

DELIMITER ;