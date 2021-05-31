USE project;
drop procedure addSupplierInvoiceLine;

DELIMITER //
CREATE PROCEDURE addSupplierInvoiceLine(IN inv_id int, prod_id int, line_quant int)
BEGIN
declare line_num int default (ifnull((select max(line_number) from supplier_invoice_line where invoice_id = inv_id), 0) + 1);
declare emp_id int default (0);
declare inventory_quant int default (select inventory_quantity from inventory where employee_id = emp_id and product_id = prod_id);
start transaction;
	insert into supplier_invoice_line values(line_num, inv_id, prod_id, line_quant);
    if prod_id is not null then
		if inventory_quant is null then
			call addInventory(emp_id, prod_id, line_quant);
		else
			call updateInventory(emp_id, prod_id, inventory_quant + line_quant);
		end if;
    end if;
commit;
END //

DELIMITER ;