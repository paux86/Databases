use project;
-- drop procedure addPayment;

DELIMITER //
create procedure addPayment(IN inv_id int, pmt_amt float)
BEGIN
declare inv_bal float default (select invoice_balance from customer_invoice where invoice_id = inv_id);
start transaction;
	insert into payment values (null, inv_id, pmt_amt, now());
    if inv_bal is not null then
		if (inv_bal - pmt_amt) >= 0 and (inv_bal - pmt_amt) < 1 then
			update customer_invoice set invoice_balance = 0.00 where invoice_id = inv_id;
		else
			update customer_invoice set invoice_balance = inv_bal - pmt_amt where invoice_id = inv_id;
		end if;
	end if;
    if inv_bal is not null and (select invoice_balance from customer_invoice where invoice_id = inv_id) >= 0 then
		commit;
	else
		rollback;
	end if;
END //

DELIMITER ;