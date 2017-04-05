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
insert into recipes values (2, 'Banana Sour Cream Bread', 'http://images.media-allrecipes.com/userphotos/720x405/262277.jpg', 'http://allrecipes.com/recipe/6984/banana-sour-cream-bread/');
insert into recipes values (3, 'Sweet Potato Chili', 'http://images.media-allrecipes.com/userphotos/720x405/903799.jpg', 'http://allrecipes.com/recipe/6984/banana-sour-cream-bread/');

insert into ingredients values (1, 'onion');
insert into ingredients values (2, 'garlic');
insert into ingredients values (3, 'basil');
insert into ingredients values (4, 'sugar');
insert into ingredients values (5, 'oregano');
insert into ingredients values (6, 'salt');
insert into ingredients values (7, 'tomato');
insert into ingredients values (8, 'tomato paste');
insert into ingredients values (9, 'sour cream');
insert into ingredients values (10, 'eggs');
insert into ingredients values (11, 'noodles');
insert into ingredients values (12, 'cheese');
insert into ingredients values (13, 'cinnamon');
insert into ingredients values (14, 'butter');
insert into ingredients values (15, 'vanilla');
insert into ingredients values (16, 'baking soda');
insert into ingredients values (17, 'flour');
insert into ingredients values (18, 'walnut');
insert into ingredients values (19, 'banana');
insert into ingredients values (20, 'potato');
insert into ingredients values (21, 'tomato sauce');
insert into ingredients values (22, 'celery');
insert into ingredients values (23, 'corn');
insert into ingredients values (24, 'black beans');
insert into ingredients values (25, 'cumin');
insert into ingredients values (26, 'ground turkey');
insert into ingredients values (27, 'ground beef');
insert into ingredients values (28, 'chili');


insert into relations values (1, 1);
insert into relations values (1, 2);
insert into relations values (1, 3);
insert into relations values (1, 4);
insert into relations values (1, 5);
insert into relations values (1, 6);
insert into relations values (1, 7);
insert into relations values (1, 8);
insert into relations values (1, 9);
insert into relations values (1, 10);
insert into relations values (1, 11);
insert into relations values (1, 12);
insert into relations values (2, 4);
insert into relations values (2, 6);
insert into relations values (2, 9);
insert into relations values (2, 10);
insert into relations values (2, 13);
insert into relations values (2, 14);
insert into relations values (2, 15);
insert into relations values (2, 16);
insert into relations values (2, 17);
insert into relations values (2, 18);
insert into relations values (2, 19);
insert into relations values (3, 1);
insert into relations values (3, 6);
insert into relations values (3, 7);
insert into relations values (3, 13);
insert into relations values (3, 20);
insert into relations values (3, 21);
insert into relations values (3, 22);
insert into relations values (3, 23);
insert into relations values (3, 24);
insert into relations values (3, 25);
insert into relations values (3, 26);
insert into relations values (3, 27);
insert into relations values (3, 28);