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
        Detail_page(k, page_url, minimum_stock)
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


def Detail_page(nomber, url ,minimum_stock):
  session = HTMLSession()
  d_r = session.get(url)
  d_soup = BeautifulSoup(d_r.content, "html.parser")

  #以下データ取得
  quantity = get_quantity.Get_quantity(d_soup)
  if quantity <= int(minimum_stock):
    print("01")
    print(url)
    pass
  else:
    asin = get_asin.Get_asin(d_soup)
    if asin == "情報なし":
      print("02")
      print(url)
      pass
    else:
      title = get_title.Get_title(d_soup)
      if title == "情報なし":
        print("03")
        print(url)
        pass
      else:
        price = get_price.Get_price(d_soup)
        if price == "情報なし":
          print("04")
          print(url)
          pass
        else:
          image = get_image.Get_images(d_soup, nomber)
          if image == "情報なし":
            print("05")
            print(url)
            pass
          else: 
            save.Save_data(nomber, asin, url, title, price, image, quantity)
  #以上データ取得
    
  time.sleep(0.2)