USE project;
drop view unassignedAppointments;

CREATE VIEW unassignedAppointments AS
SELECT appointment_id as `Id`, appointment.customer_id as `Customer Id`, customer_name as `Name`, customer_zip as `Zip Code`, customer_address as `Address`, customer_phone as `Phone #`, appointment.employee_id as `Employee Id`, employee_name as `Employee`, appointment_description as `Description`, appointment_date as `Date` 
FROM appointment 
LEFT JOIN customer ON appointment.customer_id = customer.customer_id 
LEFT JOIN employee ON appointment.employee_id = employee.employee_id
WHERE appointment.employee_id is null;