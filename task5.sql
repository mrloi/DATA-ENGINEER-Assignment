--1.How many unique values are in variable X?

SELECT COUNT(DISTINCT uniqExact(variable_X)) AS unique_values_count
FROM your_clickhouse_table;

--2.What is the average of variable Y grouped by variable Z?

SELECT variable_Z, AVG(variable_Y) AS average_Y
FROM your_clickhouse_table
GROUP BY variable_Z;