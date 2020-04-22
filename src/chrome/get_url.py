import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import os, sys, time
 
def Get_url(search_word):
  # ブラウザ操作
  options = Options()
  driver = webdriver.Chrome(chrome_options=options)
  url = "https://www.amazon.co.jp/"
  driver.get(url)
  time.sleep(3)
  element = driver.find_element_by_id("twotabsearchtextbox")
  element.send_keys(search_word)
  element.submit()
  search_url = driver.current_url
  time.sleep(5)
  driver.quit()
  time.sleep(0.5)
  return search_url
  # ブラウザ操作