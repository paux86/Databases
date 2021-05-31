USE project;

DROP PROCEDURE getEmployeeInventory;

DELIMITER //
CREATE PROCEDURE getEmployeeInventory(IN employeeId int(11))
BEGIN
	SELECT inventory.employee_id as `Employee Id`, employee.employee_name as `Employee Name`, product.product_id as `Product ID`, product.product_name as `Product Name`, product.product_description as `Description`, inventory_quantity as `Inventory Total` FROM inventory
	JOIN employee ON inventory.employee_id = employee.employee_id
	JOIN product ON inventory.product_id = product.product_id
    WHERE
    CASE
		WHEN employeeId IS NOT NULL THEN (inventory.employee_id = employeeId)
        ELSE (inventory.employee_id >= 0)
	END;
END //

DELIMITER ;