-- Add composite index on location and record_date
ALTER TABLE ClimateData 
ADD INDEX idx_location_date (location, record_date);

-- Add index on temperature
ALTER TABLE ClimateData 
ADD INDEX idx_temperature (temperature);

-- Add index on precipitation
ALTER TABLE ClimateData 
ADD INDEX idx_precipitation (precipitation);

-- Optional: Add index on record_date (helpful for time-based filtering)
ALTER TABLE ClimateData 
ADD INDEX idx_record_date (record_date);
