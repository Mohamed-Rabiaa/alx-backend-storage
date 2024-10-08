-- creates a table users With these attributes:
-- id: integer, never null, auto increment and primary key
-- email: string (255 characters), never null and unique
-- name, string (255 characters)
CREATE TABLE IF NOT EXISTS users (
       id INTEGER NOT NULL AUTO_INCREMENT,
       email VARCHAR(255) NOT NULL UNIQUE,
       name VARCHAR(255),
       PRIMARY KEY (id)
       );
       
