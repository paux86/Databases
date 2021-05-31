USE project;
-- drop procedure updateProduct;

DELIMITER //
CREATE PROCEDURE updateProduct(IN prod_id int, sup_id int, prod_name varchar(50), prod_cost float, prod_desc varchar(100))
BEGIN
	update product
    set supplier_id = sup_id, product_name = prod_name, product_cost = prod_cost, product_description = prod_desc
    where product_id = prod_id;
END //

DELIMITER ;