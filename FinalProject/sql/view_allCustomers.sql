USE project;

CREATE VIEW allCustomers AS
SELECT customer_id as `Id`, customer_name as `Name`, customer_phone as `Phone #`, customer_zip as `Zip Code`, customer_address as `Address`, customer_lastService as `Last Service`, customer_appointmentReminders as `Reminder (Days)` FROM customer;