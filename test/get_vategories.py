import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession


ct_text = ""
url = "https://www.amazon.co.jp/%E6%AD%AF%E8%BB%8A%E3%83%91%E3%83%BC%E3%83%84-500g-%E7%B4%84360%E5%80%8B%E3%82%BB%E3%83%83%E3%83%88-%E3%82%AF%E3%83%A9%E3%83%95%E3%83%88-%E3%83%81%E3%83%A3%E3%83%BC%E3%83%A0/dp/B079DJ8NS6/ref=sr_1_3?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&crid=P1UICUPIZHYZ&keywords=%E9%83%A8%E5%93%81&qid=1582508388&sprefix=%E9%83%A8%E5%93%81%2Caps%2C1245&sr=8-3"

session = HTMLSession()
r = session.get(url)
d_soup = BeautifulSoup(r.content, "html.parser")
ct_boxs = d_soup.select(".a-link-normal.a-color-tertiary", recursive=False)
for ct_box in ct_boxs:
  # print(ct_box.get_text().replace('\n','').replace(' ',''))
  ct_text = ct_text + str(ct_box.get_text().replace('\n','').replace(' ','')) + " ? "
print(ct_text[:-3])

