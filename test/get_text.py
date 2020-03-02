import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession

url = "https://www.amazon.co.jp/%E8%85%95%E6%99%82%E8%A8%88%E3%83%99%E3%83%AB%E3%83%88%E3%83%94%E3%83%B3-%E3%82%A6%E3%82%A9%E3%83%83%E3%83%81%E3%82%B9%E3%83%97%E3%83%AA%E3%83%B3%E3%82%B0%E3%83%90%E3%83%BC-%E3%82%B9%E3%83%88%E3%83%A9%E3%83%83%E3%83%97%E3%83%AA%E3%83%B3%E3%82%AF%E3%83%94%E3%83%B3-%E3%82%B9%E3%83%97%E3%83%AA%E3%83%B3%E3%82%B0%E3%83%90%E3%83%BC%E3%83%94%E3%83%B3%E3%83%AA%E3%83%A0%E3%83%BC%E3%83%90%E3%83%BC-18%E3%82%B5%E3%82%A4%E3%82%BA%EF%BC%888-25mm%EF%BC%89/dp/B07ZPSRS3R/ref=sr_1_2?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&keywords=%E9%83%A8%E5%93%81&qid=1583151458&sr=8-2"

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