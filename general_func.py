import unittest
from selenium import webdriver

class GeneralFuncTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/')

    def test_JSCALC001(self):
        self.assertIn('Calculator', self.driver.title)

    def test_JSCALC002(self):
        self.assertIn('.', self.driver.find_element_by_class_name('calculator'))
        self.assertIn('0', self.driver.find_element_by_class_name('calculator'))
        self.assertIn('1', self.driver.find_element_by_class_name('calculator'))
        self.assertIn('2', self.driver.find_element_by_class_name('calculator'))
        self.assertIn('3', self.driver.find_element_by_class_name('calculator'))
        self.assertIn('4', self.driver.find_element_by_class_name('calculator'))
        self.assertIn('5', self.driver.find_element_by_class_name('calculator'))
        self.assertIn('6', self.driver.find_element_by_class_name('calculator'))
        self.assertIn('7', self.driver.find_element_by_class_name('calculator'))
        self.assertIn('8', self.driver.find_element_by_class_name('calculator'))
        self.assertIn('9', self.driver.find_element_by_class_name('calculator'))
        self.assertIn('+', self.driver.find_element_by_class_name('calculator'))
        self.assertIn('-', self.driver.find_element_by_class_name('calculator'))
        self.assertIn('&times;', self.driver.find_element_by_class_name('calculator'))
        self.assertIn('&divide', self.driver.find_element_by_class_name('calculator'))
        self.assertIn('C', self.driver.find_element_by_class_name('calculator'))

    def test_JSCALC007(self):
        self.driver.find_element_by_id('btn-3').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div').click()
        assert '3+' in self.driver.find_element_by_id('input').text
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[2]').click()
        assert '3-' in self.driver.find_element_by_id('input').text
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[3]').click()
        assert '3&times;' in self.driver.find_element_by_id('input').text
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[4]').click()
        assert '3&divide;' in self.driver.find_element_by_id('input').text

    def test_JSCALC008(self):
        self.driver.find_element_by_class_name('btn-5').click()
        self.driver.find_element_by_class_name('btn-4').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[4]').click()
        self.driver.find_element_by_id('btn-9').click()
        self.driver.find_element_by_id('result').click()
        self.driver.find_element_by_id('btn-3').click()
        assert '3' in self.driver.find_element_by_id('input').text

    def tearDown(self):
        self.driver.quit()


