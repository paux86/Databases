use project;

DELIMITER //
create procedure customerBilled(IN inv_id int)
BEGIN
update customer_invoice set invoice_billed = now() where invoice_id = inv_id;
END //
DELIMITER ;