# This is the main server script that will start the server when run
# 
# Provides API calls to:
#   - Search recipes by name
#   - Search recipes by ingredient IDs
#   - Search ingredients by name
#   - Update recipe 'like' count
# 
# Created by Sage Thomas 2/20/2017

from flask import Flask, jsonify, abort, make_response, request

app = Flask(__name__)

# Test recipes
recipes = [
  {
    'id': 1,
    'name': u'Grilled Cheese',
    'likes': 4,
    'url': 'http://allrecipes.com/recipe/23891/grilled-cheese-sandwich/'
  },
  {
    'id': 2,
    'name': u'Pasta',
    'likes': 3,
    'url': 'http://allrecipes.com/recipe/19907/awesome-bow-tie-pasta/'
  }
]

# Test ingredients
ingredients = [
  {
    'id': 1,
    'name': u'Bread'
  },
  {
    'id': 2,
    'name': u'Cheese'
  },
  {
    'id': 3,
    'name': u'Butter'
  },
  {
    'id': 4,
    'name': u'Chicken'
  },
  {
    'id': 5,
    'name': u'Olive Oil'
  },
  {
    'id': 6,
    'name': u'Pasta'
  },
  {
    'id': 7,
    'name': u'Onion'
  },
  {
    'id': 8,
    'name': u'Vinegar'
  },
  {
    'id': 9,
    'name': u'Tomato'
  }
]

# Required relations for testing
# Essential is only marked True if known
relations = [
  {
    'recipe_id': 1,
    'ingredient_id': 1,
    'essential': True
  },
  {
    'recipe_id': 1,
    'ingredient_id': 2,
    'essential': True
  },
  {
    'recipe_id': 1,
    'ingredient_id': 3,
    'essential': False
  },
  {
    'recipe_id': 2,
    'ingredient_id': 2,
    'essential': False
  },
  {
    'recipe_id': 2,
    'ingredient_id': 5,
    'essential': False
  },
  {
    'recipe_id': 2,
    'ingredient_id': 6,
    'essential': True
  },
  {
    'recipe_id': 2,
    'ingredient_id': 7,
    'essential': False
  },
  {
    'recipe_id': 2,
    'ingredient_id': 8,
    'essential': False
  },
  {
    'recipe_id': 2,
    'ingredient_id': 9,
    'essential': False
  }
]

# Search recipes by name or ingredient IDs
# ex: '/recipes/search?name=chicken' --> search for recipes with 'chicken' in the name
# ex: '/recipes/search?ids=1,2' --> search for recipes that use ingredients 1 and 2
@app.route('/recipes/search', methods=['GET'])
def search_recipes():
  name = request.args.get('name')
  ids_str = request.args.get('ids')

  return None

# Search ingredients by name
# ex: '/recipes/search?name=chicken' --> search for ingredients with 'chicken' in the name
@app.route('/ingredients/search', methods=['GET'])
def search_ingredients():
  name = request.args.get('name').lower()
  ingr = {}
  for ingredient in ingredients:
    if ingredient['name'].lower() == name:
      ingr = ingredient

  return jsonify(ingr)

# Update recipes 'like' count
# ex: '/recipes?id=1&like=1' --> add 1 like to recipe with id 1
@app.route('/recipe', methods=['PUT'])
def update_recipe_likes():
  id_str = request.args.get('name')
  like_str = request.args.get('like')
  
  return None

# Test Route
@app.route('/')
def index():
  return "Hello, World!"

@app.errorhandler(404)
def not_found(error):
  return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
  app.run(debug=True)
