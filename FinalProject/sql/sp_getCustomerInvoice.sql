USE project;
drop procedure getCustomerInvoice;

DELIMITER //
CREATE PROCEDURE getCustomerInvoice(IN inv_id int)
BEGIN
	select line_number as `Line`, invoice_id as `Invoice`, product.product_id as `Product Id`, product.product_name as `Product Name`, service.service_id as `Service Id`, service.service_name as `Service Name`, line_quantity as `Quantity`, round(ifnull(product.product_cost, 0) + ifnull(service.service_price, 0), 2) * line_quantity as `Line Total` from customer_invoice_line
	left join product on customer_invoice_line.product_id = product.product_id
	left join service on customer_invoice_line.service_id = service.service_id
	where invoice_id = inv_id;
END //

DELIMITER ;