USE project;

create view allSuppliers as
select supplier_id as `Id`, supplier_name as `Name`, supplier_phone as `Phone`, supplier_email as `Email` from supplier;