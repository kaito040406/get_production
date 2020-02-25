import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import urllib.error
import urllib.request

url = "https://www.amazon.co.jp/%E3%83%99%E3%83%93%E3%83%BC%E3%82%B9%E3%83%9E%E3%82%A4%E3%83%AB-%E3%80%90S-503%E3%80%91%E3%83%A1%E3%83%AB%E3%82%B7%E3%83%BC%E3%83%9D%E3%83%83%E3%83%88%E7%94%A8-%E9%83%A8%E5%93%81%E3%83%BB%E6%B6%88%E8%80%97%E5%93%81-%E3%83%95%E3%83%AD%E3%83%BC%E3%83%88%E3%82%BB%E3%83%83%E3%83%88/dp/B07B5TP8CN/ref=sr_1_54_sspa?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&keywords=%E9%83%A8%E5%93%81&qid=1582628496&sr=8-54-spons&psc=1&smid=A22UCQTK6U22BD&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUFEMk1GVVJIOUNYR0UmZW5jcnlwdGVkSWQ9QTAwOTk5NDUxOFRDVUlLV1Q0WThUJmVuY3J5cHRlZEFkSWQ9QTNQRzlDOEVSQUhDOE4md2lkZ2V0TmFtZT1zcF9idGYmYWN0aW9uPWNsaWNrUmVkaXJlY3QmZG9Ob3RMb2dDbGljaz10cnVl"

session = HTMLSession()
r = session.get(url)
d_soup = BeautifulSoup(r.content, "html.parser")
quantity_boxs= d_soup.select(".a-size-medium.a-color-price", recursive=False)

for quantity_box in quantity_boxs:
  check_word = quantity_box.get_text().replace('\n','').replace(' ','')
  if '残り' in check_word:
    if '点' in check_word[3]:
      quantity = check_word[2]
    else:
      quantity = check_word[2:4]


