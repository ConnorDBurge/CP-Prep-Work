create view daily_summaries as
select 
  	stations.name, 
	reports.time::date,
	min(tempf) as min_tempf, 
    max(tempf) as max_tempf,
	min(humidity) as min_humidity, 
    max(humidity) as max_humidity,
	min(wind_speed) as min_wind_speed,  
    max(wind_speed) as max_wind_speed
from reports
join stations on reports.station_id=stations.id
group by 1, 2
order by 1, 2;
