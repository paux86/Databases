USE project;
drop procedure addCustomerInvoiceLine;

DELIMITER //
CREATE PROCEDURE addCustomerInvoiceLine(IN inv_id int, prod_id int, serv_id int, line_quant int)
BEGIN
declare line_num int default (ifnull((select max(line_number) from customer_invoice_line where invoice_id = inv_id), 0) + 1);
declare emp_id int default (select employee_id from customer_invoice where invoice_id = inv_id);
declare inv_bal float default (ifnull((select invoice_balance from customer_invoice where invoice_id = inv_id), 0));
declare inv_tot float default (ifnull((select invoice_total from customer_invoice where invoice_id = inv_id), 0));
start transaction;
	insert into customer_invoice_line values(line_num, inv_id, prod_id, serv_id, line_quant);
    if prod_id is not null then
    call updateInventory(emp_id, prod_id, (select inventory_quantity from inventory where employee_id = emp_id and product_id = prod_id) - line_quant);
    update customer_invoice set invoice_total = inv_tot + ((select product_cost from product where product_id = prod_id) * line_quant) where invoice_id = inv_id;
    update customer_invoice set invoice_balance = inv_bal + ((select product_cost from product where product_id = prod_id) * line_quant) where invoice_id = inv_id;
    else
    update customer_invoice set invoice_total = inv_tot + ((select service_price from service where service_id = serv_id) * line_quant) where invoice_id = inv_id;
    update customer_invoice set invoice_balance = inv_bal + ((select service_price from service where service_id = serv_id) * line_quant) where invoice_id = inv_id;
    end if;
if prod_id is null or (select inventory_quantity from inventory where employee_id = emp_id and product_id = prod_id) >= 0 then
commit;
else rollback;
end if;
END //

DELIMITER ;