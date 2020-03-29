import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession
import datetime


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
      dt_now = datetime.datetime.now()
    else:
      print(arrive_time_text[0].get_text()[0:9].replace(' ',''))
      if int(arrive_time_text[0].get_text()[5]) < 10:
        manth = arrive_time_text[0].get_text()[0:4] + "/0" + arrive_time_text[0].get_text()[5:9].replace(' ','')
        print(manth)
      else:
        manth = arrive_time_text[0].get_text()[0:9].replace(' ','')
    
      if int(manth[8] + manth[9]) < 10:
        day = manth[0:6] + "/0" + manth[8:9].replace(' ','')
      else:
        day = manth
      dt_now = datetime.datetime.now()
      print(day)
  except IndexError:
    print("NG")