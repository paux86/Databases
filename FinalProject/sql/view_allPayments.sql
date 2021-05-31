use project;

create view allPayments as
select payment_id as `Payment Id`, invoice_id as `Invoice Id`, payment_amount as `Amount`, payment_date as `Date` from payment;