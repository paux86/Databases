USE project;
drop view allSupplierInvoice;

CREATE VIEW allSupplierInvoice AS
SELECT invoice_id as `Invoice Id`, supplier_id as `Supplier Id`, invoice_date as `Invoice Date` from supplier_invoice;