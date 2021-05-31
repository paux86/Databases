USE project;
-- drop procedure addSupplier;

DELIMITER //
CREATE PROCEDURE addSupplier(IN id int, name varchar(50), phone int, email varchar(50))
BEGIN
	insert into supplier values(id, name, phone, email);
END //

DELIMITER ;