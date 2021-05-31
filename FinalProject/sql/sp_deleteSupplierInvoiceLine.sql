USE project;
drop procedure deleteSupplierInvoiceLine;

DELIMITER //
CREATE PROCEDURE deleteSupplierInvoiceLine(IN line int, inv_id int, prod_id int, line_quant int)
BEGIN
declare emp_id int default (0);
start transaction;
	delete from supplier_invoice_line where line_number = line and invoice_id = inv_id;
    if prod_id is not null then
    call updateInventory(emp_id, prod_id, (select inventory_quantity from inventory where employee_id = emp_id and product_id = prod_id) - line_quant);
    end if;
commit;
END //

DELIMITER ;