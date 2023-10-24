--Create a PostgreSQL database 
CREATE DATABASE PostgreSQL;

--Create a table.
CREATE TABLE tetuan_city_power_consumption (
    date_time TIMESTAMP,
    temperature FLOAT,
    humidity FLOAT,
    wind_speed FLOAT,
    general_diffuse_flows FLOAT,
    diffuse_flows FLOAT,
    zone_1_power_consumption FLOAT,
    zone_2_power_consumption FLOAT,
    zone_3_power_consumption FLOAT
);


--Store the cleaned dataset
COPY tetuan_city_power_consumption FROM 'Tetuan City power consumption.csv' WITH CSV HEADER;

