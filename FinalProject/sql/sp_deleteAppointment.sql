USE project;

DELIMITER //
CREATE PROCEDURE deleteAppointment(IN pk int)
BEGIN
	delete from appointment where appointment_id = pk;
END //

DELIMITER ;