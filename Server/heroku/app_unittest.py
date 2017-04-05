import unittest
import json
import requests

class AppTest(unittest.TestCase):

  def setUp(self):
    pass

  def is_connection(self, url):
    response_data = None
    try:
      response_data = requests.get(url)
    except:
      pass
    return bool(response_data)

  def get_json(self, url):
    json_data = None
    try:
      response = requests.get(url)
      json_data = json.loads(response.text)
    except:
      return False
    return json_data
  
  def is_json(self, data):
    is_json = False
    if type(data) is list or type(data) is dict:
      is_json = True
    return is_json

  def test_root_connection(self):
    self.assertTrue(self.is_connection('http://recipist-csci3308.herokuapp.com'))

  def test_search_connection(self):
    self.assertTrue(self.is_connection('http://recipist-csci3308.herokuapp.com/search'))

  def test_home_is_json(self):
    self.assertTrue(self.is_json(self.get_json('http://recipist-csci3308.herokuapp.com')))

  def test_search_is_json(self):
    self.assertTrue(self.is_json(self.get_json('http://recipist-csci3308.herokuapp.com/search?ingrds=banana')))

if __name__ == '__main__':
  unittest.main()
