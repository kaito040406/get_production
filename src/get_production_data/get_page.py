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
from .get_param import arrive
sys.path.append('../')
from save_data import save


def get_data(url, search_number, minimum_stock, prime_check, minimum_review, together_check, *ng_word):
  k = 1
  j = 1
  num = 0
  check = ""
  while num == 0: 
    session = HTMLSession()
    r = session.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    datas = soup.select(".s-expand-height.s-include-content-margin.s-border-bottom", recursive=False)
    for data in datas:
      url_datas = data.select(".a-link-normal.a-text-normal", recursive=False)
      try:
        url = url_datas[0].get("href")
        page_url = "https://www.amazon.co.jp/"+url
        if page_url != check:

          # 在庫調査
          stock = data_filter.Get_quantity_indexPage(data)
          
          # 合わせ買い調査
          if together_check == True:
            buying_together = data_filter.Buying_together(data)
          else:
            buying_together = False

          # レビュー調査
          try:
            review = data.select(".a-icon-alt", recursive=False)[0].get_text()[-3:]
            float_review = float(review)
          except IndexError:
            float_review = 0.0

          #  NGワード調査
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

          # リードタイム取得
          arrive_time = arrive.Get_arrive(data)

          if prime_check == True and len(data.select(".aok-relative.s-icon-text-medium.s-prime", recursive=False)) != 0 and float_review >= float(minimum_review) and stock >= int(minimum_stock) and buying_together == False and title_path == True and arrive_time == True:
            count_check = Detail_page(j, page_url, minimum_stock, *ng_word)
            if count_check == True:
              j = j + 1
            time.sleep(0.3)
          elif prime_check == False and float_review >= float(minimum_review) and stock >= int(minimum_stock) and buying_together == False and title_path == True and arrive_time == True:
            count_check = Detail_page(j, page_url, minimum_stock, *ng_word)
            if count_check == True:
              j = j + 1
            time.sleep(0.3)
          else:
            pass

          time.sleep(0.2)
         
          k = k + 1
        check = page_url 
      except IndexError:
        pass

      if k == search_number + 1:
        #return "end"
        return True

    try:
      next_page = soup.select(".a-last", recursive=False)
      next_page_url = next_page[0].find("a").get("href")
      # print("次のページ")
      url = "https://www.amazon.co.jp/" + next_page_url
      time.sleep(0.2)
    except AttributeError:
      #return "end"
      return True
      


def Detail_page(nomber, url ,minimum_stock, *ng_word):
  session = HTMLSession()
  d_r = session.get(url)
  d_soup = BeautifulSoup(d_r.content, "html.parser")

  #以下データ取得
  quantity = get_quantity.Get_quantity(d_soup)
  if quantity <= int(minimum_stock):
    print("在庫バリテーション ")
    print(url)
    return False
  else:
    asin = get_asin.Get_asin(d_soup)
    if asin == "情報なし":
      print("ASINバリテーション ")
      print(url)
      return False
    else:
      title = get_title.Get_title(d_soup, *ng_word)
      if title == "情報なし":
        print("タイトルバリテーション ")
        print(url)
        return False
      else:
        price = get_price.Get_price(d_soup)
        if price == "情報なし":
          print("金額バリテーション ")
          print(url)
          return False
        else: 
          text = get_text.Get_text(d_soup, *ng_word[3])
          if text == "情報なし":
            print("テキストバリテーション ")
            print(url)
            return False
          else:
            category = get_category.Get_category(d_soup)
            if category == "情報なし":
              print("カテゴリーバリテーション ")
              print(url)
              return False
            else:
              maker = get_maker.Get_maker(d_soup)
              if maker == "情報なし":
                print("メーカーバリテーション ")
                print(url)
                return False
              else:
                image = get_image.Get_images(d_soup, nomber)
                if image == "情報なし":
                  print("画像バリテーション")
                  print(url)
                  return False
                else:
                  save.Save_data(nomber, asin, url, title, price, image, quantity, text, category, maker)
                  return True
  #以上データ取得
    
  time.sleep(0.2)