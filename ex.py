import pandas as pd
from bs4 import BeautifulSoup
import requests
import random
import time
from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import sys
import os

options = webdriver.ChromeOptions()
options.add_argument(" — incognito")
options.headless=True

driver = webdriver.Chrome("PATH TO CHROME 8", options=options)
options = webdriver.ChromeOptions()
options.add_argument(" — incognito")

driver.get(link)
driver.close()
