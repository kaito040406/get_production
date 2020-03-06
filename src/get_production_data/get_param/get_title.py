import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession

def Get_title(d_soup, *ng_title):
  title_box = d_soup.select(".a-size-large#productTitle", recursive=False)
  if len(title_box) == 0:
    title_box = d_soup.select("#ebooksProductTitle", recursive=False)
    if len(title_box) == 0:
      title = "情報なし"
    else:
      title = title_box[0].get_text().replace('\n','').replace(' ','').replace(',','')
  else:
    title = title_box[0].get_text().replace('\n','').replace(' ','').replace(',','')
  

  for valid_title in ng_title[0]:
    if valid_title in title:
      title = "情報なし"
      break
    else:
      for title_space in ng_title[1]:
        title = title.replace(str(title_space),' ')
      for title_del in ng_title[2]:
        title = title.replace(str(title_del),'')

  return title