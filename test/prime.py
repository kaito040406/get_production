import sys
import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession


url = "https://www.amazon.co.jp/s?k=%E9%83%A8%E5%93%81&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&ref=nb_sb_noss_1"
k = 1
num = 0
check = ""
session = HTMLSession()
r = session.get(url)
soup = BeautifulSoup(r.content, "html.parser")
datas = soup.select(".a-section.a-spacing-medium", recursive=False)
for data in datas:
  prime_data = data.select(".aok-relative.s-icon-text-medium.s-prime", recursive=False)
  if len(prime_data) != 0:
    url_datas = data.select(".a-link-normal.a-text-normal", recursive=False)
    url = url_datas[0].get("href")
    print("https://www.amazon.co.jp/" + url)
  else:
    pass
  time.sleep(0.5)


    # page_url = "https://www.amazon.co.jp/"+datas2
    # if page_url != check:
    #   time.sleep(0.5)
    #   k = k + 1
    # check = page_url 

  # next_page = soup.select(".a-last", recursive=False)
  # next_page_url = next_page[0].find("a").get("href")
  # # print("次のページ")
  # url = "https://www.amazon.co.jp/" + next_page_url
  # time.sleep(0.2)