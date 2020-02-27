import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import urllib.error
import urllib.request
# import lxml.html
# import selenium.webdriver
# from selenium.webdriver.common.action_chains import ActionChains
# import chromedriver_binary
# from selenium import webdriver

def Image_download(url, nomber):
  dst_path = "images/"+ str(nomber)
  try:
    with urllib.request.urlopen(url) as web_file:
      data = web_file.read()
      with open(dst_path, mode='wb') as local_file:
          local_file.write(data)
  except urllib.error.URLError as e:
    print(e)
    pass




image_url = []
i = 1

# driver = webdriver.Chrome()
url = "https://www.amazon.co.jp/s?k=%E9%83%A8%E5%93%81&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&ref=nb_sb_noss_1"
# driver = selenium.webdriver.PhantomJS()
# driver.get(url)

# time.sleep(1)
# graph = driver.find_element_by_class_name("a-spacing-small")
# print(graph)
# actions = ActionChains(driver)
# actions.move_to_element(graph).perform()
# # actions.move_to_element(
# #     driver.find_element_by_class_name("a-spacing-small")
# # ).perform()
# # driver.find_element_by_class_name("imageThumbnail").click()
# # driver.find_element_by_class_name("a-list-item").click()
# driver.find_element_by_class_name("a-button-inner").click()
# time.sleep(5)
# r = driver.page_source.encode('utf-8')
# r = driver.page_source
# image_boxs = driver.find_element_by_class_name("imgTagWrapper")
# driver.save_screenshot("ss.png")

session = HTMLSession()
r = session.get(url)
d_soup = BeautifulSoup(r.content, "html.parser")
review_boxs = d_soup.select(".a-color-price", recursive=False)
# print(image_boxs)
# print(len(image_boxs))
# driver.close()
for review_box in review_boxs:
  if "残り" in review_box.get_text():
    if '点' in review_box.get_text()[3]:
      print(review_box.get_text()[2])
    else:
      print(review_box.get_text()[2:4])
  time.sleep(0.1)



