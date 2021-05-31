USE project;
-- drop view allCustomerInvoice;

CREATE VIEW allCustomerInvoice AS
SELECT invoice_id as `Invoice Id`, customer_id as `Customer Id`, employee_id as `Employee Id`, invoice_date as `Invoice Date`, invoice_total as `Total`, invoice_balance as `Balance`, invoice_billed as `Billing Date` from customer_invoice;