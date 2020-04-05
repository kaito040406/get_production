import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import datetime
import re


image_url = []
i = 1
url = "https://www.amazon.co.jp/s?k=%E9%83%A8%E5%93%81&__mk_ja_JP=%E3%82%AB%E3%82%BF%E3%82%AB%E3%83%8A&ref=nb_sb_noss"


session = HTMLSession()
r = session.get(url)
d_soup = BeautifulSoup(r.content, "html.parser")
datas = d_soup.select(".s-expand-height.s-include-content-margin.s-border-bottom", recursive=False)



for review_box in datas:
  time.sleep(1.0)
  arrive_time = review_box.select(".a-row.s-align-children-center", recursive=False)
  try:
    arrive_time_text = arrive_time[0].select(".a-text-bold", recursive=False)
    if "明日中" in arrive_time_text[0].get_text():
      print(arrive_time_text[0].get_text())
    else:
      now = datetime.datetime.now()
      # print(arrive_time_text[0].get_text())
      date = re.findall(r'\d+', arrive_time_text[0].get_text())
      # print(date)
      # print(now)

      arrive = datetime.date(int(date[0]), int(date[1]), int(date[2]))
      nowday = datetime.date(now.year, now.month, now.day)
 
      print((arrive-nowday).days)
      # a = datetime.date(2015, 4, 1)
      # b = datetime.date(2016, 1, 25)
      # print((b-a).days)

      # print((datetime.date(integer(date[0]), date[1], date[2])-datetime.date(now.year, now.month, now.day)).day)

      # if len(arrive_time_text[0].get_text()) < 10:
      #   now = datetime.datetime.now()
      #   manth = arrive_time_text[0].get_text()[0:4] + "/0" + arrive_time_text[0].get_text()[5:9].replace(' ','')
      # else:
      #   manth = arrive_time_text[0].get_text()[0:9].replace(' ','')
      
    
      # if (len(manth) == 9):
      #   day = manth[0:7] + "/0" + manth[8:9].replace(' ','')
      # else:
      #   day = manth

      # nowDate = datetime.date.today()
      # print(nowDate)
      # print(day.replace('/','-'))

      # getting_year = int(manth[0:3])
      # if(manth[5] == "0"):
      #   getting_manth = int(manth[6])
      # else:
        # getting_day = int(manth[5] + manth[6])

      # dt1 = datetime(int(nowDate[0:3]),nodata[],1)
      # dt2 = datetime(2018,10,1)
  except IndexError:
    print("NG")