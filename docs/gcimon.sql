create table projects (
    project_id INTEGER PRIMARY KEY,
    project_name TEXT,
    project_status INTEGER,
    project_backend STRING,
    project_host STRING,
    project_last REAL,
    project_state INTEGER
);

-- insert into projects values (null,'GCI Monitor Dummy Project',1,'hudson','http://localhost:8080/hudson',20081212.3,1);

