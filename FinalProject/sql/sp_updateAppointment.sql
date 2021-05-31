USE project;
drop procedure updateAppointment;

DELIMITER //
CREATE PROCEDURE updateAppointment(IN appt_id int, cust_id int, emp_id int, appt_desc varchar(100), appt_date datetime)
BEGIN
	update appointment
    set customer_id = cust_id, employee_id = emp_id, appointment_description = appt_desc, appointment_date = appt_date
    where appointment_id = appt_id;
END //

DELIMITER ;