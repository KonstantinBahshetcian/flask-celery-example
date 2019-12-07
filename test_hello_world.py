import app
import unittest

class TestHelloWorld(unittest.TestCase):

    def setUp(self):
        self.app = app.app.test_client()
        self.app.testting = True

    def test_statsu_code(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_greeting_message(self):

if __name__ == '__main__':
    unnitest.main()