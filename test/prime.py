import sys
import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from .get_param import get_quantity
from .get_param import get_asin
from .get_param import get_title
from .get_param import get_price
from .get_param import get_image
sys.path.append('../')
from save_data import save


def get_data(url, search_number, minimum_stock):
  k = 1
  num = 0
  check = ""
  while num == 0: 
    session = HTMLSession()
    r = session.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    datas = soup.select(".a-link-normal.a-text-normal", recursive=False)
    for data in datas:
      datas2 = data.get("href")
      page_url = "https://www.amazon.co.jp/"+datas2
      if page_url != check:
        # print(str(k) + "件目")
      
        time.sleep(0.5)
        k = k + 1
      check = page_url 
      if k == search_number + 1:
        return "end"

    next_page = soup.select(".a-last", recursive=False)
    next_page_url = next_page[0].find("a").get("href")
    # print("次のページ")
    url = "https://www.amazon.co.jp/" + next_page_url
    time.sleep(0.2)