import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession


def Get_maker(d_soup):
  maker_boxs = d_soup.select(".a-link-normal#bylineInfo", recursive=False)
  try:
    maker = ">" +  str(maker_boxs[0].get_text())
    return maker

  except IndexError:
    return "情報なし"