from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json

service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)

with open("connect.json") as f:
    Json = json.load(f)

driver.get(Json['url'])
driver.maximize_window()
