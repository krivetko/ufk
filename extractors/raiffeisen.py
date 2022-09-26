from datetime import datetime, timezone, timedelta
import pytz
from fake_useragent import UserAgent
from bs4 import BeautifulSoup

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import re

from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
co = ChromeOptions()

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
localtime = pytz.timezone("Asia/Krasnoyarsk")
fua = UserAgent(verify_ssl=False)
headers = {'User-Agent': fua.random}

class Extractor:
    __scraped_data = None
    __url = None

    def __init__(self, url):
        self.__url = url 

    def get_data(self, delta = 30):
        
        if self.__scraped_data is not None:

            startdate = datetime.utcnow().replace(hour=0, minute=0, second=0, microsecond=0, tzinfo=localtime) - timedelta(delta)
            output_list = []
        
            for section in self.__scraped_data:
                section_data = [e for e in section[1] if e[1] >= startdate]
                if len(section_data) > 0:
                    output_list.append([section[0], section_data])

            return output_list
        else:
            return []

    def __get_date(self, tag):
        dates = re.search('(?P<date>\d{2}.\d{2}.\d{4})', tag)
        times = re.search('(?P<time>\d{2}:\d{2})', tag)
        dtstring = '01.01.1970 00:00'
        if dates is not None:
            dtstring = dates['date']
            if times is not None:
                dtstring = dtstring + ' ' + times['time']
            else:
                dtstring = dtstring + ' 00:00'
        return localtime.localize(datetime.strptime(dtstring, '%d.%m.%Y %H:%M'))
        
    def __extract_element(self, doc):
        href = self.__domain + doc['href']
        text = doc.text
        date_p = doc.find('p')
        if date_p:
            date = self.__get_date(date_p.text)
        else:
            date = self.__get_date(text)
        return (text, date, href)

    def __parse_contents(self, soup, caption):
        doclist = []
        for doc in soup.select('div.list_files div:not(.more_list) a'):
            result = self.__extract_element(doc)
            if result:
                doclist.append(result)
        if len(doclist) > 0:
            if self.__scraped_data is None:
                self.__scraped_data = [] 
                self.__scraped_data.append([caption, doclist])
            else:
                self.__scraped_data.append([caption, doclist])

    def scrape(self):
        driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub', options=co)
        driver.get(self.__url)
        s = re.findall('(https?://[A-Za-z_0-9.-]+)/.*', driver.current_url)
        self.__domain = s[0]
        s = re.search('INFO_SUBSECTION(?P<section>\d*)-(?P<value>\d*)', self.__url)
        pif_menu = driver.find_element(By.XPATH, '//*[text()="Паевые инвестиционные фонды"]/../..')
        filter_list = driver.find_element(By.XPATH, '//option[@value = "{}" and @data-section = "{}"]'.format(s['value'], s['section']))
        fund_name = filter_list.get_property('text')
        caption = pif_menu.find_element(By.XPATH, './/li[contains(@class, "active")]').text
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        self.__parse_contents(soup, caption)
        menu_elements = [e.text for e in pif_menu.find_elements(By.XPATH, './/li[not(contains(@class, "active"))]')]
        for element in menu_elements:
            menu_item = driver.find_element(By.XPATH, '//*[text()="{}"]/..'.format(element))
            try:
                menu_item.click()
                
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"global__preloader")]')))

                WebDriverWait(driver, 30).until_not(EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"global__preloader")]')))

                #element_invisible = EC.invisibility_of_element((By.XPATH, '//div[contains(@class,"global__preloader")]'))
                #WebDriverWait(driver, 10).until(element_invisible)
                filter_ = driver.find_element(By.XPATH, '//select[@data-key="INFO_FUND"]/..')
                filter_.click()
                element_present = EC.presence_of_element_located((By.XPATH, '//ul[contains(@class,"scroll-scroll_visible")]'))
                #WebDriverWait(driver, 10).until(element_invisible)
                WebDriverWait(driver, 10).until(element_present)
                fund = driver.find_element(By.XPATH, f'//li[@data-prop="INFO_FUND" and text()="{fund_name}"]')
                fund.click()
                #WebDriverWait(driver, 10).until(element_invisible)
                WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"global__preloader")]')))

                WebDriverWait(driver, 30).until_not(EC.presence_of_element_located((By.XPATH, '//div[contains(@class,"global__preloader")]')))
            except TimeoutException:
                pass
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            self.__parse_contents(soup, element)
        driver.quit()
