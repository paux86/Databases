USE project;
drop procedure addSupplierInvoice;

DELIMITER //
CREATE PROCEDURE addSupplierInvoice(IN sup_id int)
BEGIN
	insert into supplier_invoice values(null, sup_id, now());
    insert into supplier_invoice_line values(1, last_insert_id(), null, 0);
END //

DELIMITER ;