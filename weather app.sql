CREATE DATABASE weather_app;

USE weather_app;

CREATE TABLE weather (
    id INT AUTO_INCREMENT PRIMARY KEY,
    city VARCHAR(50),
    country VARCHAR(10),
    temperature FLOAT,
    feels_like FLOAT,
    humidity INT,
    `condition` TEXT,
    wind_speed FLOAT,
    timestamp DATETIME
);
