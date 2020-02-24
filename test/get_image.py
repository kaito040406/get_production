import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession


image_url = []
i = 1

session = HTMLSession()

time.sleep(1)
url = "https://www.amazon.co.jp/%E6%AD%AF%E8%BB%8A%E3%83%91%E3%83%BC%E3%83%84-500g-%E7%B4%84360%E5%80%8B%E3%82%BB%E3%83%83%E3%83%88-%E3%82%AF%E3%83%A9%E3%83%95%E3%83%88-%E3%83%81%E3%83%A3%E3%83%BC%E3%83%A0/dp/B079DJ8NS6/ref=sr_1_1?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&keywords=%E9%83%A8%E5%93%81&qid=1582512169&sr=8-1"
r = session.get(url)
d_soup = BeautifulSoup(r.content, "html.parser")
image_boxs = d_soup.select(".a-dynamic-image#landingImage", recursive=False)

for image_box in image_boxs:
  for image in image_box.get("data-a-dynamic-image").split('"'):
    if 'https://' in image:
      image_url.append(image)
      print(image)
      i += 1
    if i > 3:
      break
    time.sleep(0.2)
  time.sleep(0.2)