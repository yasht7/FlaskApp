import os
import unittest

from app import app

class BasicTests(unittest.TestCase):
    # use to initialize the database and other init stuff
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        self.app = app.test_client()

        self.assertEqual(app.debug, False)

    # executed after each test
    # you can delete the database adn do other stuff here.
    def tearDown(self):
        pass

# TESTS
    def test_home_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
