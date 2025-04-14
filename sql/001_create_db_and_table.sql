-- Create the database `project_db`
CREATE DATABASE IF NOT EXISTS project_db;

-- Use the newly created database
USE project_db;

-- Create the ClimateData table `ClimateData`
CREATE TABLE IF NOT EXISTS ClimateData (
    record_id INT PRIMARY KEY AUTO_INCREMENT,
    location VARCHAR(100) NOT NULL,
    record_date DATE NOT NULL,
    temperature FLOAT NOT NULL,
    precipitation FLOAT NOT NULL
);
