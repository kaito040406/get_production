import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession

def Get_text(d_soup, ng_words_text):
  k = 0
  review_boxs = d_soup.select(".a-unordered-list.a-vertical.a-spacing-none", recursive=False)
  for review_box in review_boxs:
    row_text = review_box.get_text().replace('\n','。').replace(' ','')
    row_texts = row_text.split('。')
    for row_text in row_texts:
      if row_text != '':
        append_text = row_text.replace('\t','')+"\n"
        print(k)
        print(append_text)
        for ng_word in ng_words_text:
          if ng_word in append_text:
            append_text = ""
          else:
            pass
          # print(append_text)
        texts = texts + append_text
        k = k +1
      else:
        pass
  
  if texts=="":
    return "情報なし"
  else:
    return texts