from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options=webdriver.ChromeOptions()
options.add_experimental_option('detach',True)

driver=webdriver.Chrome(options=options)
driver.get("https://www.amazon.in/")