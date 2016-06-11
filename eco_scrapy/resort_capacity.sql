select p.property_name, d.day, d.date, d.type from eco_day d, eco_property p, eco_month m 
where p.eid = m.eid
and m.pid = p.pid
and m.mid = d.mid
and m.eid = (select max(eid) from eco_execution_run)
and date between "2016-07-01" and "2016-07-31"
order by p.property_name, d.date;
