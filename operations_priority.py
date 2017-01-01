import unittest
from selenium import webdriver

class GeneralFuncTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/')

    def test_JSCALC038(self):
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div').click()
        self.driver.find_element_by_class_name('btn-4').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[3]').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"]/div').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[2]').click()
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_class_name('btn-5').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[4]').click()
        self.driver.find_element_by_id('btn-3').click()
        self.driver.find_element_by_id('result').click()
        assert '33' in self.driver.find_element_by_id('input').text

    def test_JSCALC039(self):
        self.driver.find_element_by_id('btn-9').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[4]').click()
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"]/div[2]').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[3]').click()
        self.driver.find_element_by_class_name('btn-4').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"]/div').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[2]').click()
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_id('btn-9').click()
        self.driver.find_element_by_id('result').click()
        assert '8' in self.driver.find_element_by_id('input').text

    def test_JSCALC0409(self):
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[3]').click()
        self.driver.find_element_by_class_name('btn-4').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[3]').click()
        self.driver.find_element_by_id('btn-6').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[4]').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"]/div[2]').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div').click()
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_id('btn-6').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[2]').click()
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[3]').click()
        self.driver.find_element_by_class_name('btn-5').click()
        self.driver.find_element_by_id('result').click()
        assert '12' in self.driver.find_element_by_id('input').text

    def tearDown(self):
        self.driver.quit()
