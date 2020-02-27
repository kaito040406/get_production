import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession


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

def Buying_together(data):
  try:
    buying_together_text = data.select(".a-size-base.s-addon-highlight-color.s-highlighted-text-padding.aok-inline-block")[0].get_text()
    if "あわせ買い" in buying_together_text:
      buying_together = True
    else:
      buying_together = False

    return buying_together

  except IndexError:
    buying_together = False

    