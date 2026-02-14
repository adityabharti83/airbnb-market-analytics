-- 1) Make sure no one is using the DB
USE master;
GO

ALTER DATABASE AirbnbMarketAnalytics
SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
GO

-- 2) Drop the database
DROP DATABASE AirbnbMarketAnalytics;
GO

CREATE DATABASE AirbnbMarketAnalytics;
GO
