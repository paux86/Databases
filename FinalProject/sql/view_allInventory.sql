USE project;
drop view allInventory;

CREATE VIEW allInventory AS
SELECT product.product_id as `Product ID`, product.product_name as `Product Name`, product.product_description as `Description`, sum(inventory_quantity) as `Inventory Total` FROM inventory
JOIN employee ON inventory.employee_id = employee.employee_id
JOIN product ON inventory.product_id = product.product_id
GROUP BY inventory.product_id;