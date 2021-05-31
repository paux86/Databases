USE project;
drop procedure addCustomerInvoice;

DELIMITER //
CREATE PROCEDURE addCustomerInvoice(IN cust_id int, emp_id int)
BEGIN
	insert into customer_invoice values(null, cust_id, emp_id, now(), 0.00, 0.00, null);
    insert into customer_invoice_line values(1, last_insert_id(), null, null, 0);
END //

DELIMITER ;