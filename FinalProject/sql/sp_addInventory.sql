USE project;

DELIMITER //
CREATE PROCEDURE addInventory(IN emp_id int, prod_id int, quant int)
BEGIN
	insert into inventory values(emp_id, prod_id, quant);
END //

DELIMITER ;