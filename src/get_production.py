import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from save_data import save

def get_data(url, search_number):
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
        Detail_page(k, page_url)
        time.sleep(0.2)
        k = k + 1
      check = page_url 
      if k == search_number + 1:
        return "end"

    next_page = soup.select(".a-last", recursive=False)
    next_page_url = next_page[0].find("a").get("href")
    # print("次のページ")
    url = "https://www.amazon.co.jp/" + next_page_url
    time.sleep(0.5)


def Detail_page(nomber, url):
  session = HTMLSession()
  d_r = session.get(url)
  d_soup = BeautifulSoup(d_r.content, "html.parser")

  #以下データ取得
  asin = Get_asin(d_soup)
  title = Get_title(d_soup)
  price = Get_price(d_soup)
  #以上データ取得

  save.Save_data(nomber, asin, url, title, price)
  time.sleep(0.2)


def Get_asin(d_soup):
  asin = ""
  asin_box = d_soup.select(".pdTab", recursive=False)
  if len(asin_box) == 0:
    asin_box_3 = d_soup.select(".content", recursive=False)
    for asin_check_1 in asin_box_3:
      asin_box_2 = asin_check_1.find_all("li")
      for asin_check_2 in asin_box_2:
        asin_check_3 = asin_check_2.get_text()
        if 'ASIN' in asin_check_3:
          asin = asin_check_3[6:]
      if asin == "":
        asin_box_4 = d_soup.select("#detail_bullets_id", recursive=False)[0].find_all("li")
        for asin_check in asin_box_4:
          if 'ASIN' in asin_check.get_text():
            asin = asin_check.get_text()[6:]
  elif len(asin_box) == 1:
    asin = asin_box[0].select(".value", recursive=False)[3].get_text()
  else:
    asin_text = asin_box[1].select(".label", recursive=False)
    l = 0
    for asin_text_check in asin_text:
      if asin_text_check.get_text() == 'ASIN':
        asin = asin_box[1].select(".value", recursive=False)[l].get_text()
      l = l + 1
  if asin == "":
    asin = "情報なし"
  
  return asin


def Get_title(d_soup):
  title_box = d_soup.select(".a-size-large#productTitle", recursive=False)
  if len(title_box) == 0:
    title_box = d_soup.select("#ebooksProductTitle", recursive=False)
    if len(title_box) == 0:
      title = "情報なし"
    else:
      title = title_box[0].get_text().replace('\n','').replace(' ','').replace(',','')
  else:
    title = title_box[0].get_text().replace('\n','').replace(' ','').replace(',','')
  
  return title


def Get_price(d_soup):
  price_box = d_soup.select("#price_inside_buybox", recursive=False)
  if len(price_box) == 0:
    price_box = d_soup.select(".a-size-medium.a-color-price.offer-price.a-text-normal", recursive=False)
    if len(price_box) == 0:
      price_box = d_soup.select(".a-size-large.a-color-price.a-text-bold", recursive=False)
      if len(price_box) == 0:
        price_box = d_soup.select(".a-size-medium.a-color-price.priceBlockBuyingPriceString", recursive=False)
        if len(price_box) == 0:
          price = "情報なし"
        else:
          price = price_box[0].get_text().replace('\n','').replace(' ','').replace('￥','').replace(',','').replace('(税込)','').replace('¥','')
      else:
        price = price_box[0].get_text().replace('\n','').replace(' ','').replace('￥','').replace(',','').replace('(税込)','').replace('¥','')
    else:
      price = price_box[0].get_text().replace('\n','').replace(' ','').replace('￥','').replace(',','').replace('(税込)','').replace('¥','')
  else:
    price = price_box[0].get_text().replace('\n','').replace(' ','').replace('￥','').replace(',','').replace('(税込)','').replace('¥','')

  return price






