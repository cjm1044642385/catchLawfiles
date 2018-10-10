# coding = utf-8

import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.common.action_chains import  ActionChains
import time
chrome_options = webdriver.ChromeOptions()
#chrome_options.add_argument('--headless')
chrome_options.add_argument("--start-maximized")
browser = webdriver.Chrome(chrome_options=chrome_options)

class WenshuSpider(scrapy.Spider):		
	name = 'wsw'
	allowed_domains = ['wenshu.court.gov.cn']
	start_urls = ['http://wenshu.court.gov.cn/List/List?sorttype=1&conditions=searchWord+1+AJLX++%E6%A1%88%E4%BB%B6%E7%B1%BB%E5%9E%8B:%E5%88%91%E4%BA%8B%E6%A1%88%E4%BB%B6']
	def start_requests(self):
		browser.get(self.start_urls[0])
		yield scrapy.Request(self.start_urls[0],callback = self.parse)

	def parse(self,response):
		time.sleep(5)
		quanxuan = browser.find_element_by_name("ckall")
		quanxuan.click()
		time.sleep(5)
		xiazai = browser.find_element_by_id("operate").find_element_by_xpath("div[2]")
		ActionChains(browser).click(xiazai).perform()
		time.sleep(5)

		

