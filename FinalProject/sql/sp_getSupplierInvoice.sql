USE project;
drop procedure getSupplierInvoice;

DELIMITER //
CREATE PROCEDURE getSupplierInvoice(IN inv_id int)
BEGIN
	select line_number as `Line`, invoice_id as `Invoice`, product.product_id as `Product Id`, product.product_name as `Product Name`, line_quantity as `Quantity` from supplier_invoice_line
	left join product on supplier_invoice_line.product_id = product.product_id
	where invoice_id = inv_id;
END //

DELIMITER ;