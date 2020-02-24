import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession

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