import unittest
from selenium import webdriver

class GeneralFuncTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get('http://test.job.klika-tech.com.s3-website.eu-central-1.amazonaws.com/')

    def test_JSCALC009(self):
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div').click()
        self.driver.find_element_by_id('btn-3').click()
        self.driver.find_element_by_id('result').click()
        assert '5' in self.driver.find_element_by_id('input').text

    def test_JSCALC010(self):
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div').click()
        self.driver.find_element_by_id('btn-6').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"]/div[2]').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div[2]').click()
        self.driver.find_element_by_id('btn-9').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"]/div').click()
        self.driver.find_element_by_id('result').click()
        assert '70.97' in self.driver.find_element_by_id('input').text

    def test_JSCALC011(self):
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_class_name('btn-4').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div[2]').click()
        self.driver.find_element_by_id('btn-6').click()
        self.driver.find_element_by_class_name('btn-4').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div').click()
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_class_name('btn-5').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div[2]').click()
        self.driver.find_element_by_id('btn-3').click()
        self.driver.find_element_by_id('btn-6').click()
        self.driver.find_element_by_id('result').click()
        assert '30' in self.driver.find_element_by_id('input').text

    def test_JSCALC012(self):
        self.driver.find_element_by_class_name('btn-5').click()
        self.driver.find_element_by_id('btn-6').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div[2]').click()
        self.driver.find_element_by_id('btn-3').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"]/div').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div[2]').click()
        self.driver.find_element_by_id('btn-9').click()
        self.driver.find_element_by_id('result').click()
        assert '64.2' in self.driver.find_element_by_id('input').text

    def test_JSCALC013(self):
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"]/div').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div').click()
        self.driver.find_element_by_id('result').click()
        assert '17' in self.driver.find_element_by_id('input').text

    def test_JSCALC014(self):
        self.driver.find_element_by_id('btn-9').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div').click()
        self.driver.find_element_by_id('result').click()
        assert '9' in self.driver.find_element_by_id('input').text

    def test_JSCALC015(self):
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div').click()
        self.driver.find_element_by_id('btn-3').click()
        self.driver.find_element_by_xpath('//div[@class="numbers"][4]/div[2]').click()
        self.driver.find_element_by_class_name('btn-5').click()
        self.driver.find_element_by_xpath('//div[@class="operators"]/div').click()
        self.driver.find_element_by_id('btn-1').click()
        self.driver.find_element_by_id('btn-2').click()
        self.driver.find_element_by_id('result').click()
        assert '17.5' in self.driver.find_element_by_id('input').text

    def test_JSCALC016(self):
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
        self.driver.find_element_by_xpath('//div[@class="operators"]/div').click()
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
        assert '44444444444444444' in self.driver.find_element_by_id('input').text

    def tearDown(self):
        self.driver.quit()

