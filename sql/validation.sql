USE project_db;

-- Validate table structure
DESCRIBE ClimateData;

-- Count records to verify data seeding
SELECT COUNT(*) AS total_records FROM ClimateData;

-- Sample queries to verify data
SELECT location, AVG(temperature) AS avg_temp, AVG(humidity) AS avg_humidity 
FROM ClimateData 
GROUP BY location 
ORDER BY avg_temp DESC;

-- Explains SELECT query 
EXPLAIN SELECT * FROM ClimateData WHERE temperature > 20;

-- Use Index on Date + Location
EXPLAIN SELECT * FROM ClimateData 
WHERE location = 'Tokyo' AND record_date BETWEEN '2025-01-10' AND '2025-01-20';

-- EXPLAIN for Aggregates
EXPLAIN SELECT AVG(temperature) FROM ClimateData 
WHERE location = 'London' AND record_date BETWEEN '2025-01-01' AND '2025-01-31';


