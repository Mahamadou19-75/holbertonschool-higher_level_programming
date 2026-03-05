-- Creates the database `hbtn_0d_usa` if it does not exist
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;

-- Ensures the `states` table exists to enforce foreign key constraints correctly
-- Note: This is a safeguard and assumes the `states` table creation is handled elsewhere or already exists.
CREATE TABLE IF NOT EXISTS states (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(256) NOT NULL
);

-- Creates the `cities` table if it does not exist
CREATE TABLE IF NOT EXISTS cities (
    id INT AUTO_INCREMENT PRIMARY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    CONSTRAINT fk_state
        FOREIGN KEY (state_id) 
        REFERENCES states(id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);
