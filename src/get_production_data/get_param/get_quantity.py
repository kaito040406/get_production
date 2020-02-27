import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession



def Get_quantity(d_soup):
  quantity_boxs= d_soup.select(".a-size-medium.a-color-price", recursive=False)

  for quantity_box in quantity_boxs:
    check_word = quantity_box.get_text().replace('\n','').replace(' ','')
    if '残り' in check_word:
      if '点' in check_word[3]:
        quantity = check_word[2]
      else:
        quantity = check_word[2:4]

  try:
    return int(quantity)

  except NameError:
    quantity_boxs2= d_soup.select(".a-size-medium.a-color-success", recursive=False)
    for quantity_box in quantity_boxs2:
      check_word = quantity_box.get_text().replace('\n','').replace(' ','')
      if '在庫' in check_word:
        quantity = 100
    try:
      return quantity

    except NameError:
      quantity = 0
      return quantity

def Get_quantity_indexPage(data):
  try:
    stock_text = data.select(".a-color-price", recursive=False)[0].get_text()
    if "残り" in stock_text:
      if "点" in stock_text[3]:
        stock = int(stock_text[2])
      else:
        stock = int(stock_text[2:4])
    else:
      stock = 100
    return stock

  except IndexError:
    stock = 100
    return stock