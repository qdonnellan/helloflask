import hello
import unittest
import os

class HelloTestCase(unittest.TestCase):
    '''
    the first test of my flask app! 

    must type "source venv/bin/activate" in command line before 
    using nosetests to get this to work apparently
    '''
    def setUp(self):
        hello.app.config['TESTING'] = True
        self.app = hello.app.test_client()

    def test_random_thing_that_should_fail(self):
        self.assertEqual(4,2)

    def test_main_app_route(self):
        response = self.app.get('/')
        self.assertIn('Hello World', response.data)