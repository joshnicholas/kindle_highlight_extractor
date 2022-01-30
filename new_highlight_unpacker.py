import pandas as pd 

from selenium import webdriver 
from selenium.webdriver.firefox.options import Options

import datetime 
import dateparser
# import pytz

import time
import re
import random 
import sys

user = sys.argv[1]
passo = sys.argv[2]

chrome_options = Options()
# # chrome_options.add_argument("--headless")

driver = webdriver.Firefox(options=chrome_options) 

linko = 'https://read.amazon.com.au/notebook'

def go_get(urlo, user, passo):
    driver.get(urlo)
    nammo = driver.find_element_by_id('ap_email').send_keys(user)
    passer = driver.find_element_by_id('ap_password').send_keys(passo)
    button = driver.find_element_by_id('signInSubmit').click()

    time.sleep(5)
    h2s = driver.find_elements_by_tag_name('h2')

    for h in h2s[30:]:

        print(h.text)
        
        stringo = ''
        highlights = []

        h.click()
        time.sleep(5)

        elements = driver.find_elements_by_id('highlight')
        
        titlo = driver.find_element_by_tag_name('h3').text
        titlo = titlo.strip()

        datter = driver.find_element_by_id('kp-notebook-annotated-date').text
        datto = dateparser.parse(datter)
        datto = datto.strftime('%y%m%d')

        print(datto)

        stringo += f"{datto} {titlo}"
        stringo += "\n\n"

        titlo = re.sub('[^A-Za-z0-9]+', '', titlo)
        print(titlo)

        for e in elements:
            highlights.append(e.text)
            stringo += e.text
            stringo += "\n\n"


        with open(f"output/{datto}{titlo}.txt", "w") as f:
            f.write(stringo)

        sleeper = 10 * random.random()
        time.sleep(sleeper)
        
        print(highlights)

go_get(linko, user, passo)
