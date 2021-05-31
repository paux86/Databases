use project;
-- drop procedure updateSupplierInvoiceLine;

DELIMITER //
create procedure updateSupplierInvoiceLine(IN line int, inv_id int, prod_id int, line_quant int)
BEGIN
call deleteSupplierInvoiceLine(line, inv_id, prod_id, line_quant);
call addSupplierInvoiceLine(inv_id, prod_id, line_quant);
update supplier_invoice_line set line_number = line where line_number = last_insert_id() and invoice_id = inv_id;
END //

DELIMITER ;