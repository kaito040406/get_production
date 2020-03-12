import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession

def Get_category(d_soup):
  ct_boxs = d_soup.select(".a-link-normal.a-color-tertiary", recursive=False)
  for ct_box in ct_boxs:
    ct_text = ct_text + str(ct_box.get_text().replace('\n','').replace(' ','')) + " ? "
  if ct_text == "":
    return "情報なし"
  else:
    return ct_text[:-3]