--select the maximum temperatures from each stat
use `hbtn_0c_0`
SELECT state, MAX(value)
FROM temperatures
GROUP BY state;