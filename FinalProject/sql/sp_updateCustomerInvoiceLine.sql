USE project;
-- drop procedure updateCustomerInvoiceLine;

DELIMITER //
CREATE PROCEDURE updateCustomerInvoiceLine(IN line int, inv_id int, prod_id int, serv_id int, line_quant int, line_total float)
BEGIN
call deleteCustomerInvoiceLine(line, inv_id, prod_id, serv_id, line_quant, line_total);
call addCustomerInvoiceLine(inv_id, prod_id, serv_id, line_quant);
update customer_invoice_line set line_number = line where line_number = last_insert_id() and invoice_id = inv_id;
END //

DELIMITER ;