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
