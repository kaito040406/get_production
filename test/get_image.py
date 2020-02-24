import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession


session = HTMLSession()

time.sleep(1)
url = "https://www.amazon.co.jp/%E6%AD%AF%E8%BB%8A%E3%83%91%E3%83%BC%E3%83%84-500g-%E7%B4%84360%E5%80%8B%E3%82%BB%E3%83%83%E3%83%88-%E3%82%AF%E3%83%A9%E3%83%95%E3%83%88-%E3%83%81%E3%83%A3%E3%83%BC%E3%83%A0/dp/B079DJ8NS6/ref=sr_1_1?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&keywords=%E9%83%A8%E5%93%81&qid=1582512169&sr=8-1"
r = session.get(url)
d_soup = BeautifulSoup(r.content, "html.parser")
image_boxs = d_soup.select(".a-dynamic-image#landingImage", recursive=False)

# image_box = image_boxs[0].get("data-old-hires")
# print(image_boxs)
# print(len(image_boxs))

for image_box in image_boxs:
  print("ああああああああああああああああああああああああああ")
  print(image_box.get("data-a-dynamic-image"))
  print(len(image_box.get("data-a-dynamic-image")))
  for image in image_box.get("data-a-dynamic-image"):
    print(image)
  time.sleep(0.2)