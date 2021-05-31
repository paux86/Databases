USE project;
drop view allEmployees;

CREATE VIEW allEmployees AS
select employee_id as `ID`, employee_name as `Name`, employee_phone as `Phone #`, employee_zip as `Zip Code`, employee_address as `Address`, employee_hourly_pay as `Hourly Rate`, employee_startDate as `Start Date`, employee_endDate as `End Date` from employee