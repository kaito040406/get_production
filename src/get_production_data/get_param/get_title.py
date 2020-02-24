import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession

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