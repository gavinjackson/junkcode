drop table if exists eco_execution_run;
drop table if exists eco_property;
drop table if exists eco_month;
drop table if exists eco_day;


create table eco_execution_run (
    eid     integer     primary key AUTOINCREMENT,
    execution_date  datetime not NULL
);

create table eco_property(
    pid integer primary key AUTOINCREMENT,
    eid integer not null,
    property_name text not NULL,
    property_webid text not NULL,
    foreign key(eid) references eco_execution_run(eid)
);

create table eco_month (
   mid integer primary key AUTOINCREMENT,
   eid integer not null,
   pid integer not null,
   month text NOT NULL,
   foreign key (eid) references eco_execution_run(eid),
   foreign key (pid) references eco_property(pid)
);

create table eco_day (
   did integer primary key AUTOINCREMENT,
   mid int not NULL,
   type text NOT NULL,
   day text NOT NULL,
   date datetime not null,
   foreign key (mid) references eco_month(mid)
);
