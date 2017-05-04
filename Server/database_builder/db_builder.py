# This is a script that uses the CSV file provided by the web crawler to create
# the database file for the production server.
# 
# Created by Sage Thomas 2/20/2017
from collections import OrderedDict

class Recipe:
  def __init__(self):
    self.id = -1
    self.name = ''
    self.url = ''
    self.image_url = ''

class Relation:
  def __init__(self, recipe_id, ingredient_id):
    self.recipe_id = recipe_id
    self.ingredient_id = ingredient_id

# f is the file to write to
def initialize(f):
  print "Initializing file..."
  tables = """create table if not exists recipes(
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

"""
  f.write(tables)
  print "Done"

# Creates the data to fill the database with
# uses CSV file created by web crawler
def create_relations():
  print "Creating relations..."
  recipes = []
  ingredients = OrderedDict()
  relations = []

  recipe_count = 1
  ingredient_count = 1
  first_line = True

  with open("recipes.csv", "r") as f:
    for line in f:
      if first_line:
        first_line = False
        continue

      parts = line.split(',')

      # Recipe
      recipe = Recipe()
      recipe.id         = recipe_count
      recipe.name       = parts[0].replace("'", '')
      recipe.url        = parts[2]
      recipe.image_url  = parts[3].strip()
      recipes.append(recipe)
      recipe_count += 1
  
      # Ingredients
      ingrs = parts[1].split('|')
      for ingr in ingrs:
        if ingr not in ingredients:
          ingredients[ingr] = ingredient_count
          ingredient_count += 1
      
      # Relations
      for ingr in ingrs:
        relations.append(Relation(recipe.id, ingredients[ingr]))
  
  print "Done"
  return (recipes, ingredients, relations)

def build_file(file_name):
  print "Creating %s, old version will be overwritten" % file_name
  f = open(file_name, "w+")

  initialize(f)

  recipes, ingredients, relations = create_relations()

  for r in recipes:
    f.write("insert into recipes values (%d, '%s', '%s', '%s');\n" % (r.id, r.name, r.image_url, r.url))

  f.write("\n")

  for key, value in ingredients.iteritems():
    f.write("insert into ingredients values (%d, '%s');\n" % (value, key))

  f.write("\n")

  for r in relations:
    f.write("insert into relations values (%d, %d);\n" % (r.recipe_id, r.ingredient_id))

  f.close() 
  print "Successfully made %s!" % file_name


if __name__ == '__main__':
  build_file("db.sql")
