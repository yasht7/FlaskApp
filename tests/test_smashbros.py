import os
import unittest

from app import app,db
from app.mod_smashbros.models import Character

TEST_DB = 'test.db'

class SmashBrosTests(unittest.TestCase):
    # use to initialize the database and other init stuff
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(app.config['BASE_DIR'], TEST_DB)
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

        self.assertEqual(app.debug, False)

    # executed after each test
    # you can delete the database and do other stuff here.
    def tearDown(self):
        db.session.remove()
        db.drop_all()


    def add_helper(self, name, weight, powers, speed):
        character = Character(name, weight, powers, speed)
        db.session.add(character)
        db.session.commit()
        return character

# TESTS
    def test_add_character(self):
        response = self.app.post('/smashbros/add_character', data=dict(name='Goku', weight=220, powers="kamehameha, instant transmission", speed=20), follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_delete_character(self):
        character = self.add_helper("Goku", 200, "Instant transmission", 100)
        character_id = db.session.query(Character).filter_by(name="Goku").first().id
        response = self.app.post('/smashbros/delete_character/%d'%character_id, follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_udpate_character(self):
        character = self.add_helper("Goku", 200, "Instant transmission", 100)

if __name__ == "__main__":
    unittest.main()
