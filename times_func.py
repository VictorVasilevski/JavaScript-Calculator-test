import unittest
from selenium import webdriver

class GeneralFuncTests(unittest.TestCase):

    def test_JSCALC017(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/')
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[3]').click()
        self.driver.find_element_by_id('btn-3').click()
        self.driver.find_element_by_id('result').click()
        assert '6' in self.driver.find_element_by_id('input').text

    def test_JSCALC018(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/')
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[3]').click()
        self.driver.find_element_by_class_name('btn-4').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div[2]').click()
        self.driver.find_element_by_id('btn-9').click()
        self.driver.find_element_by_id('result').click()
        assert '9.8' in self.driver.find_element_by_id('input').text

    def test_JSCALC019(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/')
        self.driver.find_element_by_class_name('btn-5').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div[2]').click()
        self.driver.find_element_by_class_name('btn-5').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[3]').click()
        self.driver.find_element_by_class_name('btn-4').click()
        self.driver.find_element_by_id('result').click()
        assert '22' in self.driver.find_element_by_id('input').text

    def test_JSCALC020(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/')
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"]/div').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[3]').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div').click()
        self.driver.find_element_by_id('result').click()
        assert '0' in self.driver.find_element_by_id('input').text

    def test_JSCALC021(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/')
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div[2]').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"]/div').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[3]').click()
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_id('result').click()
        assert '11.7' in self.driver.find_element_by_id('input').text

    def test_JSCALC022(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/')
        self.driver.find_element_by_id('btn-9').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[3]').click()
        self.driver.find_element_by_id('result').click()
        assert '0' in self.driver.find_element_by_id('input').text

    def test_JSCALC023(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/')
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[3]').click()
        self.driver.find_element_by_id('btn-3').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div[2]').click()
        self.driver.find_element_by_class_name('btn-5').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[3]').click()
        self.driver.find_element_by_id('btn-3').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div[3]').click()
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div').click()
        self.driver.find_element_by_id('result').click()
        assert '420' in self.driver.find_element_by_id('input').text
