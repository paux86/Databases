USE project;
DROP PROCEDURE getProductsOverInterval;

DELIMITER //
CREATE PROCEDURE getProductsOverInterval(IN pastInterval int(11))
BEGIN
	SELECT product.product_id as `Id`, product.product_name as `Name`, sum(customer_invoice_line.line_quantity) as `Total Used` FROM customer_invoice_line
    JOIN product ON customer_invoice_line.product_id=product.product_id
    JOIN customer_invoice ON customer_invoice_line.invoice_id=customer_invoice.invoice_id
    WHERE customer_invoice_line.product_id is not null AND datediff(now(), customer_invoice.invoice_date) <= pastInterval
    GROUP BY `Id`;
END //

DELIMITER ;