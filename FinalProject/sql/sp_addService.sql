USE project;

DELIMITER //
create procedure addService(IN serv_id int, serv_name varchar(50), serv_price float)
BEGIN
	insert into service values(serv_id, serv_name, serv_price);
END //

DELIMITER ;