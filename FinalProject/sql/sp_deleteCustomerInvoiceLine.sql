USE project;
drop procedure deleteCustomerInvoiceLine;

DELIMITER //
CREATE PROCEDURE deleteCustomerInvoiceLine(IN line int, inv_id int, prod_id int, serv_id int, line_quant int, line_total float)
BEGIN
declare emp_id int default (select employee_id from customer_invoice where invoice_id = inv_id);
declare inv_total float default (select invoice_total from customer_invoice where invoice_id = inv_id);
declare inv_balance float default (select invoice_balance from customer_invoice where invoice_id = inv_id);
start transaction;
	delete from customer_invoice_line where line_number = line and invoice_id = inv_id;
    update customer_invoice set invoice_balance = inv_balance - line_total, invoice_total = inv_total - line_total where invoice_id = inv_id;
    if prod_id is not null then
    call updateInventory(emp_id, prod_id, (select inventory_quantity from inventory where employee_id = emp_id and product_id = prod_id) + line_quant);
    end if;
commit;
END //

DELIMITER ;