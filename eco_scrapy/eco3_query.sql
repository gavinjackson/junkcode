select day, date, type from eco_day where mid in
(select mid from eco_month where pid in
  (select pid from eco_property where property_name = 'Ecocrackenback 3' and eid =
    (select max(eid) from eco_execution_run)
  )
)
order by date;
