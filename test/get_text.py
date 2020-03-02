import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession

url = "https://www.amazon.co.jp/%E8%85%95%E6%99%82%E8%A8%88%E3%83%99%E3%83%AB%E3%83%88%E3%83%94%E3%83%B3-%E3%82%A6%E3%82%A9%E3%83%83%E3%83%81%E3%82%B9%E3%83%97%E3%83%AA%E3%83%B3%E3%82%B0%E3%83%90%E3%83%BC-%E3%82%B9%E3%83%88%E3%83%A9%E3%83%83%E3%83%97%E3%83%AA%E3%83%B3%E3%82%AF%E3%83%94%E3%83%B3-%E3%82%B9%E3%83%97%E3%83%AA%E3%83%B3%E3%82%B0%E3%83%90%E3%83%BC%E3%83%94%E3%83%B3%E3%83%AA%E3%83%A0%E3%83%BC%E3%83%90%E3%83%BC-18%E3%82%B5%E3%82%A4%E3%82%BA%EF%BC%888-25mm%EF%BC%89/dp/B07ZPSRS3R/ref=sr_1_2?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&keywords=%E9%83%A8%E5%93%81&qid=1583151458&sr=8-2"

session = HTMLSession()
r = session.get(url)
d_soup = BeautifulSoup(r.content, "html.parser")
review_boxs = d_soup.select(".a-unordered-list.a-vertical.a-spacing-none", recursive=False)
for review_box in review_boxs:
  row_text = review_box.get_text().replace('\n','').replace(' ','')
  row_texts = row_text.split('。')
  for row_text in row_texts:
    print(row_text.replace('\t',''))
    time.sleep(0.2)