import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import datetime
import re

def Get_arrive(d_soup):
  datas = d_soup.select(".s-expand-height.s-include-content-margin.s-border-bottom", recursive=False)
  for review_box in datas:
    time.sleep(1.0)
    arrive_time = review_box.select(".a-row.s-align-children-center", recursive=False)
    try:
      arrive_time_text = arrive_time[0].select(".a-text-bold", recursive=False)
      if "明日中" in arrive_time_text[0].get_text():
        #明日取得の物は取得する
        return True
      else:
        now = datetime.datetime.now()
        date = re.findall(r'\d+', arrive_time_text[0].get_text())
        arrive = datetime.date(int(date[0]), int(date[1]), int(date[2]))
        nowday = datetime.date(now.year, now.month, now.day)
        day_difference =  (arrive-nowday).days
      
        #リードタイムが5日異常は取得しない
        if(int(day_difference) > 5):
          return False
        else:
          #上記条件意外だと取得する
          return True
    except IndexError:
      #リードタイムが書かれていないものも取得しない
      return False