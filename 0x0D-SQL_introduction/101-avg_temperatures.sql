--Find the average temperature of each city
USE `hbtn_0c_0`
select city, AVG(value) as avg_temp
FROM temperatures
GROUP BY city;