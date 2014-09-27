from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_project_and_retrieve_it_later(self):

        # Edith has heard about a cool bew online personal finance app. She 
        # goes to check out its homepage.
        self.browser.get('http://localhost:8000')
        
        # She notices the page title and header mention alchemy
        self.assertIn('Alchemy', self.browser.title) #"Browser title was " + browser.title
        
        # ...
        self.fail('Finish the test!')
        
        # Satisfied, she goes back to sleep


if __name__ == '__main__':
    unittest.main(warnings='ignore')        
