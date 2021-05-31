USE project;
-- drop procedure updateInventory;

DELIMITER //
CREATE PROCEDURE updateInventory(IN emp_id int, prod_id int, quant int)
BEGIN
	update inventory
    set inventory_quantity = quant
    where employee_id = emp_id and product_id = prod_id;
END //

DELIMITER ;