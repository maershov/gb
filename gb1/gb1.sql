create database example if not exists ;
use example;
create table users if not exists (
    id integer,
    name text
);


-- > create database example
-- [2021-10-16 13:15:30] 1 row affected in 17 ms
-- > use example
-- [2021-10-16 13:15:42] completed in 4 ms
-- example> create table users (
--              id integer,
--              name text
--          )
-- [2021-10-16 13:17:34] completed in 55 ms
-- example> create database sample
-- [202
-- 1-10-16 13:18:26] 1 row affected in 9 ms

-- C:\Program Files\MySQL\MySQL Server 8.0\bin>mysql sample < example.sql
-- C:\Program Files\MySQL\MySQL Server 8.0\bin>mysql sample < example.sql