import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import urllib.error
import urllib.request

url = "https://www.amazon.co.jp/%E8%85%95%E6%99%82%E8%A8%88%E4%BF%AE%E7%90%86%E3%82%BB%E3%83%83%E3%83%88-%E8%85%95%E6%99%82%E8%A8%88%E3%83%99%E3%83%AB%E3%83%88%E8%AA%BF%E6%95%B4-%E8%85%95%E6%99%82%E8%A8%88%E4%BF%AE%E7%90%86%E3%83%84%E3%83%BC%E3%83%AB-%E8%85%95%E6%99%82%E8%A8%88%E4%BF%AE%E7%90%86%E5%B7%A5%E5%85%B7%E3%82%BB%E3%83%83%E3%83%88-%E8%85%95%E6%99%82%E8%A8%88%E3%83%90%E3%83%B3%E3%83%89%E8%AA%BF%E6%95%B4/dp/B07THT2HS7/ref=sxbs_sxwds-stvp?__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&cv_ct_cx=%E9%83%A8%E5%93%81&keywords=%E9%83%A8%E5%93%81&pd_rd_i=B07THT2HS7&pd_rd_r=0f06d9ef-c7bd-4bb5-aafe-f165ffeb2fa7&pd_rd_w=oI5fx&pd_rd_wg=sriVJ&pf_rd_p=e29507e3-7937-4495-82f4-55b5d5ca8047&pf_rd_r=CTWSBFKKJ8N1WG2YWHQV&psc=1&qid=1582628496"

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

try:
  print(quantity)

except NameError:
  quantity_boxs2= d_soup.select(".a-size-medium.a-color-success", recursive=False)
  for quantity_box in quantity_boxs2:
    check_word = quantity_box.get_text().replace('\n','').replace(' ','')
    if '在庫' in check_word:
      quantity = check_word
  try:
    print(quantity)

  except NameError:
    quantity = "0"