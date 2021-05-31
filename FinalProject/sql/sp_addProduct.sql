USE project;

DELIMITER //
CREATE PROCEDURE addProduct(IN prod_id int, supplier_id int, prod_name varchar(50), prod_cost float, prod_desc varchar(100))
BEGIN
	insert into product values(prod_id, supplier_id, prod_name, prod_cost, prod_desc);
END //

DELIMITER ;