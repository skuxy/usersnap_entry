CREATE TABLE pizzas
(
    id integer primary key,
    name text not null,
    price float not null,
    ingredients text [],
    img text
);

CREATE TABLE extras
(
    name text primary key,
    price integer not null
);

-- \SET CONTENT `cat pizzas.json`;
-- INSERT INTO pizzas values (:'content');
-- 
-- \SET CONTENT `cat extras.json`
-- INSERT INTO extras values (:'content');
