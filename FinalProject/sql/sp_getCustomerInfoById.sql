USE project;
DROP PROCEDURE getCustomerInfoById;

DELIMITER //
CREATE PROCEDURE getCustomerInfoById(IN custId int(11))
BEGIN
	SELECT * FROM customer
    LEFT JOIN appointment ON customer.customer_id=appointment.customer_id
    LEFT JOIN customer_invoice ON customer.customer_id=customer_invoice.customer_id
    WHERE customer.customer_id=custId;
END //

DELIMITER ;