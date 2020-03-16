import sys
import requests
import time
from bs4 import BeautifulSoup
from requests_html import HTMLSession
from .data_filter import data_filter
from .get_param import get_quantity
from .get_param import get_asin
from .get_param import get_title
from .get_param import get_price
from .get_param import get_image
from .get_param import get_text
from .get_param import get_category
from .get_param import get_maker
sys.path.append('../')
from save_data import save


def get_data(url, search_number, minimum_stock, prime_check, minimum_review, together_check, *ng_word):
  k = 1
  num = 0
  check = ""
  while num == 0: 
    session = HTMLSession()
    r = session.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    print(soup)
    datas = soup.select(".s-expand-height.s-include-content-margin.s-border-bottom", recursive=False)
    for data in datas:
      url_datas = data.select(".a-link-normal.a-text-normal", recursive=False)
      try:
        url = url_datas[0].get("href")
        page_url = "https://www.amazon.co.jp/"+url
        if page_url != check:

          stock = data_filter.Get_quantity_indexPage(data)
          
          if together_check == True:
            buying_together = data_filter.Buying_together(data)
          else:
            buying_together = False

          try:
            review = data.select(".a-icon-alt", recursive=False)[0].get_text()[-3:]
            float_review = float(review)
          except IndexError:
            float_review = 0.0

          try:
            index_title = data.select(".a-size-base-plus.a-color-base.a-text-normal", recursive=False)[0].get_text()
            for ng_title in ng_word[0]:
              if ng_title in index_title:
                title_path = False
                break
              else:
                title_path = True
          except IndexError:
            title_path = True

          if prime_check == True and len(data.select(".aok-relative.s-icon-text-medium.s-prime", recursive=False)) != 0 and float_review >= float(minimum_review) and stock >= int(minimum_stock) and buying_together == False and title_path == True:
            Detail_page(k, page_url, minimum_stock, *ng_word)
            time.sleep(0.3)
          elif prime_check == False and float_review >= float(minimum_review) and stock >= int(minimum_stock) and buying_together == False and title_path == True:
            Detail_page(k, page_url, minimum_stock, *ng_word)
            time.sleep(0.3)
          else:
            pass

          time.sleep(0.2)
         
          k = k + 1
        check = page_url 
      except IndexError:
        pass

      if k == search_number + 1:
        return "end"

    try:
      next_page = soup.select(".a-last", recursive=False)
      next_page_url = next_page[0].find("a").get("href")
      # print("次のページ")
      url = "https://www.amazon.co.jp/" + next_page_url
      time.sleep(0.2)
    except AttributeError:
      return "end"
      


def Detail_page(nomber, url ,minimum_stock, *ng_word):
  session = HTMLSession()
  d_r = session.get(url)
  d_soup = BeautifulSoup(d_r.content, "html.parser")

  #以下データ取得
  quantity = get_quantity.Get_quantity(d_soup)
  if quantity <= int(minimum_stock):
    print("01")
    print(url)
    pass
  else:
    asin = get_asin.Get_asin(d_soup)
    if asin == "情報なし":
      print("02")
      print(url)
      pass
    else:
      title = get_title.Get_title(d_soup, *ng_word)
      if title == "情報なし":
        print("03")
        print(url)
        pass
      else:
        price = get_price.Get_price(d_soup)
        if price == "情報なし":
          print("04")
          print(url)
          pass
        else:
          image = get_image.Get_images(d_soup, nomber)
          if image == "情報なし":
            print("05")
            print(url)
            pass
          else: 
            text = get_text.Get_text(d_soup, *ng_word[3])
            if text == "情報なし":
              print("06")
              print(url)
              pass
            else:
              category = get_category.Get_category(d_soup)
              if category == "情報なし":
                print("07")
                print(url)
              else:
                maker = get_maker.Get_maker(d_soup)
                if maker == "情報なし":
                  print("08")
                  print(url)
                else:
                  save.Save_data(nomber, asin, url, title, price, image, quantity, text, category, maker)
  #以上データ取得
    
  time.sleep(0.2)