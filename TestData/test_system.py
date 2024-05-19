import unittest
from selenium import webdriver
from app import create_app, db
from threading import Thread

class SystemTestCase(unittest.TestCase):
    def setUp(self):
        self.app = create_app('testing')
        self.client = self.app.test_client()
        with self.app.app_context():
            db.create_all()

        self.browser = webdriver.Firefox()
        self.app_thread = Thread(target=self.app.run, kwargs={'use_reloader': False})
        self.app_thread.start()

    def tearDown(self):
        self.browser.quit()
        self.app_thread.join()
        with self.app.app_context():
            db.session.remove()
            db.drop_all()

    def test_home_page(self):
        self.browser.get('http://localhost:5000/')
        self.assertIn('Hello', self.browser.page_source)

if __name__ == '__main__':
    unittest.main()
