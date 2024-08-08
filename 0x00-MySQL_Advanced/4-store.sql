-- Creates a trigger that decreases the quantity of an item after adding a new order.
DROP TRIGGER IF EXISTS item_quantity_trigger;
CREATE TRIGGER item_quantity_trigger AFTER INSERT ON orders
        For EACH ROW
        UPDATE items
	SET quantity = quantity - NEW.number
	WHERE name = NEW.item_name;
	
