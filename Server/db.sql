create table if not exists recipes(
       id int primary key,
       name char,
       image_url text,
       url text
);
   
create table if not exists ingredients(
       id int primary key,
       name char
);
       
create table if not exists relations(
       r_id int references recipes(id),
       i_id int references ingredients(id)
);
