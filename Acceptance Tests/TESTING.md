# Testing

## Who
* Sage Thomas - ScienceSage
* Burak Karaoglu- mbkaraoglu
* Amulya Srivastava - amsr2031
* Victoria Soesanto - viso4661
* Qiu Duan - qidu0919

## Title
Recipist

## Vision
Make cooking less of a chore.

## Automated Tests
The unit test script used to test the server running on heroku is located [here](https://github.com/ScienceSage/Recipist/blob/master/Server/heroku/app_unittest.py)

This is the output:
```
C:\Users\Sage\OneDrive\CU '17 Spring\Software Tools\Recipist\Server\heroku>python app_unittest.py -v
test_home_is_json (__main__.AppTest) ... ok
test_root_connection (__main__.AppTest) ... ok
test_search_connection (__main__.AppTest) ... FAIL
test_search_is_json (__main__.AppTest) ... ok

======================================================================
FAIL: test_search_connection (__main__.AppTest)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "app_unittest.py", line 37, in test_search_connection
    self.assertTrue(self.is_connection('http://recipist-csci3308.herokuapp.com/search'))
AssertionError: False is not true

----------------------------------------------------------------------
Ran 4 tests in 1.554s

FAILED (failures=1)
```

## User Acceptance Tests
See the 3 other files in this folder.
