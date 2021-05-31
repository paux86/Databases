USE project;

DELIMITER //
CREATE PROCEDURE addAppointment(IN cust_id int, emp_id int, appt_desc varchar(100), appt_date datetime)
BEGIN
	insert into appointment values(null, cust_id, emp_id, appt_desc, appt_date);
END //

DELIMITER ;