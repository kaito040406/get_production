import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession

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
        try:
          asin_box_4 = d_soup.select("#detail_bullets_id", recursive=False)[0].find_all("li")
          for asin_check in asin_box_4:
            if 'ASIN' in asin_check.get_text():
              asin = asin_check.get_text()[6:]
        except IndexError:
          asin = "情報なし"
        
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