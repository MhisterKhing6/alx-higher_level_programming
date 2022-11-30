--select the top average temp in july and Auguest
use `hbtn_0c_0`
select city, AVG(value) as avg_temp
FROM temperatures
WHERE month = 8 OR month = 7
GROUP BY city
ORDER BY avg_temp DESC LIMIT 3;