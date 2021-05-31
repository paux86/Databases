USE project;
DROP VIEW appointmentReminders;

CREATE VIEW appointmentReminders AS
SELECT customer_name as `Name`, customer_phone as `Phone`, customer_lastService as `Last Service`, customer_appointmentReminders as `Reminder (Days)` FROM customer
WHERE customer_appointmentReminders is not NULL and datediff(now(), customer_lastService) >= customer_appointmentReminders;