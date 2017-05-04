# This is a web crawler that will search for recipes and save the results
# in a CSV file
#
# Will use allrecipes.com to crawl
# 
# Created by Sage Thomas 3/4/2017

from lxml import html
import requests

class Recipe:
  def __init__(self):
    self.name = ''
    self.ingredients = []
    self.url = ''
    self.image_url = ''
  
  def __str__(self):
    recipe = ''
    recipe += 'Name:\t\t' + self.name
    recipe += '\nIngredients:\t' + str(self.ingredients)
    recipe += '\nUrl:\t\t' + self.url
    recipe += '\nImage:\t\t' + self.image_url
    return recipe

def clean_ingredients(raws):
  black_list = ['teaspoon', 'jar', 'can', 'cup', 'light','white', 'brown', 
    'ounces', 'canned', 'sliced', 'tablespoon', 'unsweetened', 'room', 
    'temperature', 'chopped', 'distilled', 'all-purpose', 'pinch', 'pound',
    'cold', 'boiling', 'hot', 'toasted', 'envelope', 'dinner', 'package',
    'softened', 'drained', 'beaten', 'divided', 'split', 'cooked', 'shredded',
    'bittersweet', 'dry', 'roasted', 'diced', 'confectioner', 'sifted', 'paper',
    'thin', 'mix', 'ounce', 'grated', 'semisweet', 'melted', 'golden', 'large',
    'skinles', 'boneles', 'halve', 'bottle', 'lengthwise', 'hoagie', 'peeled', 
    'and', 'whole', 'container', 'frozen', 'slice', 'instant', 'oriental', 
    'flavored', 'chunky', 'lean', 'medium', 'clove', 'devil', 'heavy', 
    'cleaned', 'cleaned', 'husked', 'extra', 'segment', 'head', 'pint', 
    'prepared', 'imitation', 'minced', 'or', 'a', 'needed', 'to', 'taste', 
    'stalk', 'dried', 'processed', 'fresh', 'granular', 'small', 'bulk', 
    'cored', 'trimmed', '-', 'spear', 'thawed', 'cubed', 'bag', 'separated',
    'floret', 'dijon', 'granule', 'rinsed', 'packet', 'margarine', 'freshly',
    'seeded', 'green', 'uncooked', 'firm', 'mini', 'piece', 'crushed', 
    'crumbled', 'dash', 'cube', 'ground', 'pitted', 'chilled', 'old-fashioned',
    'individual', 'per', 'serving', 'dark', 'salted', 'unsalted', 'unbleached',
    'crumb', 'rolled', 'breast', 'liter', 'tm', 'cut', 'into', 'chunk', 
    'thinly', 'more', 'if', 'brewed', 'including', 'top', 'wedge', 'juiced',
    'in', 'square', 'snapped', 'sharp', 'bunch', 'very', 'chicken-flavored',
    'day-old', 'nutritional']
  black_list_phrases = ['or to taste', 'for decoration', 'extra firm', 
    'for garnish', 'with seasoning', 'of choice', 'juice of', 'any flavor']
  synonyms = {'ramen noodle': 'ramen', 'ranch salad dressing': 'ranch'}
  plurals = {'cookies': 'cookie', 'tomatoes': 'tomato', 'potatoes': 'potato',
    'chilies': 'chili'}
  exceptions = {'hot': 'hot dog', 'ground': 'ground beef', 
    'green': 'green chilies'}
  cleaned = []
  for raw in raws:
    clean = ''
    raw = raw.strip()
    raw = raw.lower()
    # get rid of numbers and fractions
    start = -1
    i = 0
    while i < len(raw):
      if start == -1 and raw[i].isdigit():
        start = i
      elif start != -1 and raw[i] == ' ':
        raw = raw[:start] + raw[i:]
        i = -1
        start = -1
      i += 1

    # get rid of "(" and ")" stuff inside
    start = -1
    i = 0
    while i < len(raw):
      if start == -1 and raw[i] == '(':
        start = i
      elif start != -1 and raw[i] == ')':
        raw = raw[:start] + raw[i+1:]
        start = -1
        i = 0
      i += 1
    
    # Get rid of worthless phrases
    for phrase in black_list_phrases:
      if phrase in raw:
        raw = raw.replace(phrase, '')

    raw = raw.strip()
    words = raw.split(' ')
    old_raw = raw
    raw = ''

    i = 0
    while i < len(words):
      word = words[i]
      # Get rid of punctuation
      word = word.replace(',', '')
      word = word.replace("'", '')
      word = word.replace('.', '')

      # If exception, do nothing more
      if word in exceptions:
        if exceptions[word] in old_raw:
          raw += word + ' '
          next

      # Convert common plurals
      if word in plurals:
        word = plurals[word]

      # Attempt to convert other plurals
      try:
        if word[-1] == 's':
          word = word[:-1]
          if word[-2:] == 'ie':
            word = word[:-2] + 'y'
      except:
        print "May have failed to to test " + word + " for issues"
          
      if word not in black_list:
        raw += word + ' '
      i += 1

    # Replace synonyms to most common word/phrase
    for syn in synonyms:
      if syn in raw:
        raw = raw.replace(syn, synonyms[syn])

    raw = raw.strip().replace('  ', ' ')
    # if an ingredient is salt and pepper, change to two ingredients
    if 'salt' in raw and 'pepper' in raw:
      cleaned.append('salt')
      cleaned.append('pepper')
    else:
      cleaned.append(raw)

  cleaned = list(set(cleaned))
  return cleaned

# Gather links to recipes on page

page_url = "http://allrecipes.com/recipes/157/everyday-cooking/campus-cooking/?page="
links = []
root = "http://allrecipes.com"

for p in range(1, 21):
  page = requests.get(page_url + str(p))
  tree = html.fromstring(page.content)
  links_raw = tree.xpath('//a/@href')
  for i in range(0,len(links_raw)):
    link = links_raw[i]
    if "/recipe/" in link:
      if root not in link:
        link = root + link
      tmp_link = link.strip()
      links.append(tmp_link)

links = list(set(links))
# links = ['http://allrecipes.com/recipe/44699/chocolate-cornstarch-pudding/']

# Not used or working ATM
def remove_non_ascii(s): return "".join(i for i in s if ord(i)<128)

# Make list of recipes
recipes = []
for link in links:
  recipe = Recipe()
  page = requests.get(link)
  tree = html.fromstring(page.content)

  try:
    recipe.name = tree.xpath('//h1/text()')[0].replace(',', '').strip()
    recipe.ingredients = clean_ingredients(tree.xpath('//span[@itemprop="ingredients"]/text()'))
    recipe.url = link
    recipe.image_url = tree.xpath('//img[@class="rec-photo"]/@src')[0]
    print recipe
    recipes.append(recipe)
  except Exception,e:
    print 'Error creating recipe: ' + str(e)

# Save recipes to CSV
f = open('recipes.csv', 'w')
f.write('name,ingredients,url,image url')
for r in recipes:
  try:
    f.write('\n' + r.name + ',' + '|'.join(r.ingredients) + ',' + r.url + ',' + 
    r.image_url)
  except:
    print "Failed to add recipe to CSV"
  
f.close()
