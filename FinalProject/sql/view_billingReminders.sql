USE project;
drop view billingReminders;

CREATE VIEW billingReminders AS
SELECT customer.customer_name as `Name`, customer.customer_phone as `Phone #`, customer.customer_address as `Address`, customer_invoice.invoice_id as `Invoice Number`, customer_invoice.invoice_balance as `Balance`, customer_invoice.invoice_date as `Service Date`, customer_invoice.invoice_billed as `Billing Date` FROM customer_invoice
JOIN customer ON customer_invoice.customer_id=customer.customer_id
WHERE customer_invoice.invoice_balance > 0 AND datediff(now(), customer_invoice.invoice_billed) > 30