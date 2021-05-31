USE project;
-- DROP PROCEDURE getAppointments;

DELIMITER //
CREATE PROCEDURE getAppointments(IN daysRange int, zip varchar(10), employeeId int(11))
BEGIN
	DECLARE today date default(cast(now() as date));
    IF daysRange is null THEN
		set daysRange = 1;
	END IF;
	
    SELECT appointment_id as `Id`, appointment_date as `Date`, customer_zip as `Zip Code`, customer_address as `Address`, appointment_description as `Description`, customer_name as `Name`, customer_phone as `Phone #`, employee_name as `Employee` 
	FROM appointment 
	JOIN customer ON appointment.customer_id = customer.customer_id 
	JOIN employee ON appointment.employee_id = employee.employee_id
    WHERE
    CASE
		WHEN employeeId is null and zip is null THEN (datediff(appointment_date, today) >= 0 and datediff(appointment_date, today) <= daysRange)
		WHEN zip is null THEN (datediff(appointment_date, today) >= 0 and datediff(appointment_date, today) <= daysRange AND employee.employee_id = employeeId)
		WHEN employeeId is null THEN (datediff(appointment_date, today) >= 0 and datediff(appointment_date, today) <= daysRange and customer.customer_zip = zip)
		ELSE (datediff(appointment_date, today) >= 0 and datediff(appointment_date, today) <= daysRange and employee.employee_id = employeeId and customer.customer_zip = zip)
	END;
END //

DELIMITER ;