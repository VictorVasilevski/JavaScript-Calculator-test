import unittest
from selenium import webdriver

class GeneralFuncTests(unittest.TestCase):

    def test_JSCALC025(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/')
        self.driver.find_element_by_id('btn-9').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[4]').click()
        self.driver.find_element_by_id('btn-3').click()
        self.driver.find_element_by_id('result').click()
        assert '3' in self.driver.find_element_by_id('input').text

    def test_JSCALC026(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/')
        self.driver.find_element_by_xpath('//div[@class="numbers"]/div[2]').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[4]').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div').click()
        self.driver.find_element_by_id('result').click()
        assert 'Infinity' in self.driver.find_element_by_id('input').text

    def test_JSCALC027(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/')
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[4]').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div').click()
        self.driver.find_element_by_id('result').click()
        assert 'NaN' in self.driver.find_element_by_id('input').text

    def test_JSCALC028(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/')
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_id('btn-3').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[4]').click()
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_id('btn-3').click()
        self.driver.find_element_by_id('result').click()
        assert '1' in self.driver.find_element_by_id('input').text

    def test_JSCALC029(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/')
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div[2]').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"]/div').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[4]').click()
        self.driver.find_element_by_id('result').click()
        assert 'Infinity' in self.driver.find_element_by_id('input').text

    def test_JSCALC030(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/')
        self.driver.find_element_by_xpath('//div[@class="numbers"]/div[2]').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"]/div[2]').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[4]').click()
        self.driver.find_element_by_class_name('btn-4').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div[2]').click()
        self.driver.find_element_by_class_name('btn-4').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[4]').click()
        self.driver.find_element_by_class_name('btn-4').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[4]').click()
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_id('result').click()
        assert '2.5' in self.driver.find_element_by_id('input').text

    def test_JSCALC031(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/')
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[4]').click()
        self.driver.find_element_by_id('btn-3').click()
        self.driver.find_element_by_id('result').click()
        assert '33.333333333333333' in self.driver.find_element_by_id('input').text