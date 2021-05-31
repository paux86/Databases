USE project;

CREATE VIEW allProducts AS
SELECT product_id as `Id`, supplier_id as `Supplier Id`, product_name as `Name`, product_cost as `Cost per unit`, product_description as `Description` FROM product;