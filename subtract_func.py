import unittest
from selenium import webdriver

class GeneralFuncTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/')

    def test_JSCALC032(self):
        self.driver.find_element_by_id('btn-9').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[2]').click()
        self.driver.find_element_by_id('btn-3').click()
        self.driver.find_element_by_id('result').click()
        assert '6' in self.driver.find_element_by_id('input').text

    def test_JSCALC033(self):
        self.driver.find_element_by_xpath('//div[@class="numbers"]/div[2]').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[2]').click()
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_id('btn-9').click()
        self.driver.find_element_by_id('result').click()
        assert '-11' in self.driver.find_element_by_id('input').text

    def test_JSCALC034(self):
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div[2]').click()
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[2]').click()
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div[2]').click()
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_id('result').click()
        assert '0' in self.driver.find_element_by_id('input').text

    def test_JSCALC035(self):
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div[2]').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"]/div').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[2]').click()
        self.driver.find_element_by_id('result').click()
        assert '21.7' in self.driver.find_element_by_id('input').text

    def test_JSCALC036(self):
        self.driver.find_element_by_class_name('btn-5').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"]/div').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[2]').click()
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"]/div[2]').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div[2]').click()
        self.driver.find_element_by_id('btn-9').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[2]').click()
        self.driver.find_element_by_class_name('btn-4').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[2]').click()
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div').click()
        self.driver.find_element_by_id('result').click()
        assert '24.1' in self.driver.find_element_by_id('input').text

    def test_JSCALC037(self):
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[2]').click()
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_id('result').click()
        assert '-22222222222222222' in self.driver.find_element_by_id('input').text

    def tearDown(self):
        self.driver.quit()
