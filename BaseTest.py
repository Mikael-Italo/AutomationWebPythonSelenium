from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import json

with open("connect.json") as f:
    Json = json.load(f)

service = Service('./chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get(Json["url"])

driver.close()
