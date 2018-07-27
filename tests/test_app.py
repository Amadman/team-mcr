from app import app
import unittest

class MainTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def tearDown(self):
        pass

    def test_home_status_code(self):
        result = self.app.get('/')
        self.assertEqual(result.status_code, 200)

    def test_about_status_code(self):
        result = self.app.get('/about')
        self.assertEqual(result.status_code, 200)

    def test_lang_en_status_code(self):
        result = self.app.get('/lang/en')
        self.assertEqual(result.status_code, 302)

    def test_lang_es_status_code(self):
        result = self.app.get('/lang/es')
        self.assertEqual(result.status_code, 302)

    def test_not_found_status_code(self):
        result = self.app.get('/notfound')
        self.assertEqual(result.status_code, 404)
