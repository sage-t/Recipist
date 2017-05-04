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
insert into recipes values (3, 'Sweet Potato Chili', 'http://images.media-allrecipes.com/userphotos/720x405/903799.jpg', 'http://allrecipes.com/recipe/229081/sweet-potato-chili/');
insert into recipes values (4, 'Shrimp Scampi with Pasta', 'http://images.media-allrecipes.com/userphotos/600x600/2606852.jpg', 'http://allrecipes.com/recipe/229960/shrimp-scampi-with-pasta/');
insert into recipes values (5, 'Chicken Francesa', 'http://images.media-allrecipes.com/userphotos/720x405/2179438.jpg', 'http://allrecipes.com/recipe/241716/chicken-francesa/');
insert into recipes values (6, 'Farmer Casserole', ' http://images.media-allrecipes.com/userphotos/250x250/159442.jpg', 'http://allrecipes.com/recipe/22454/farmers-casserole/');
insert into recipes values (7, 'Simple Garlic Shrimp', 'http://images.media-allrecipes.com/userphotos/560x315/1330843.jpg', 'http://allrecipes.com/recipe/220597/simple-garlic-shrimp/');
insert into recipes values (8, 'Slow Cooker Salsa Chicken', 'http://images.media-allrecipes.com/userphotos/560x315/1096403.jpg', 'http://allrecipes.com/recipe/236128/slow-cooker-salsa-chicken/');
insert into recipes values (9, 'Asia Orange Chicken', 'http://images.media-allrecipes.com/userphotos/560x315/1207689.jpg', 'http://allrecipes.com/recipe/61024/asian-orange-chicken/');
insert into recipes values (10, 'Oven-Roasted Asparagus', 'http://images.media-allrecipes.com/userphotos/560x315/1001600.jpg', 'http://allrecipes.com/recipe/214931/oven-roasted-asparagus/');

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
insert into ingredients values (29, 'shrimp');
insert into ingredients values (30, 'lemon');
insert into ingredients values (31, 'olive oil')
insert into ingredients values (32, 'pasta')
insert into ingredients values (33, 'chicken breast')
insert into ingredients values (34, 'milk')
insert into ingredients values (35, 'white wine')
insert into ingredients values (36, 'ham')
insert into ingredients values (37, 'carrot')
insert into ingredients values (38, 'salsa')
insert into ingredients values (39, 'vinegar')
insert into ingredients values (40, 'soy sauce')
insert into ingredients values (41, 'asparagus')

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
insert into relations values (4, 2);
insert into relations values (4, 14);
insert into relations values (4, 29);
insert into relations values (4, 30);
insert into relations values (4, 31);
insert into relations values (4, 32);
insert into relations values (5, 6);
insert into relations values (5, 30);
insert into relations values (5, 33);
insert into relations values (5, 34);
insert into relations values (5, 35);
insert into relations values (6, 1);
insert into relations values (6, 6);
insert into relations values (6, 10);
insert into relations values (6, 12);
insert into relations values (6, 20);
insert into relations values (6, 34);
insert into relations values (6, 36);
insert into relations values (7, 2);
insert into relations values (7, 14);
insert into relations values (7, 29);
insert into relations values (7, 30);
insert into relations values (8, 1);
insert into relations values (8, 7);
insert into relations values (8, 22);
insert into relations values (8, 37);
insert into relations values (8, 38);
insert into relations values (9, 1);
insert into relations values (9, 6);
insert into relations values (9, 17);
insert into relations values (9, 30);
insert into relations values (9, 33);
insert into relations values (9, 39);
insert into relations values (9, 40);
insert into relations values (10, 2);
insert into relations values (10, 6);
insert into relations values (10, 12);
insert into relations values (10, 30);
insert into relations values (10, 31);
insert into relations values (10, 41);
