create table if not exists recipes(
       id int primary key,
       name varchar(30),
       image_url text,
       url text
);
   
create table if not exists ingredients(
       id int primary key,
       name varchar(30)
);
       
create table if not exists relations(
       r_id int references recipes(id),
       i_id int references ingredients(id)
);

insert into recipes values (1, 'American Lasagna', 'http://images.media-allrecipes.com/userphotos/600x600/566639.jpg', 'http://allrecipes.com/recipe/11729/american-lasagna/');

insert into ingredients values (1, 'onion');
insert into ingredients values (2, 'garlic');
insert into ingredients values (3, 'basil');
insert into ingredients values (4, 'sugar');
insert into ingredients values (5, 'oregano');
insert into ingredients values (6, 'salt');
insert into ingredients values (7, 'tomato');
insert into ingredients values (8, 'tomato paste');
insert into ingredients values (9, 'salt');

insert into relations values (1, 1);
insert into relations values (1, 2);
insert into relations values (1, 3);
insert into relations values (1, 4);
insert into relations values (1, 5);
insert into relations values (1, 6);
insert into relations values (1, 7);
insert into relations values (1, 8);
insert into relations values (1, 9); 