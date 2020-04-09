import os, sys, time
from get_production_data import get_page
from save_data import save
from output_csv import output_csv
import csv
import datetime
import eel
from chrome import get_url
import shutil


@eel.expose
def start(search_word, search_number, stock, review, prime, together):
  # バリテーション
  if(search_word == "" or search_number.isdecimal() == False or int(search_number) <= 0):
    return False
  else:
    # バリテーション終わり
    search_url = get_url.Get_url(search_word)

    save.Save_title()

    # NGワード読み込みはじまり クソコード
    title_validation = [] 
    text_validation = []
    title_space = []
    title_delete = []
    ng_word = []
    with open('NG_WORD.csv') as f:
      reader = csv.reader(f)
      for row in reader:
        if row[0] != "":
          title_validation.append(row[0])
        if row[1] != "":
          title_space.append(row[1])
        if row[2] != "":
          title_delete.append(row[2])
        if row[3] != "":
          text_validation.append(row[3])
    f.close()
    ng_word.append(title_validation)
    ng_word.append(title_space)
    ng_word.append(title_delete)
    ng_word.append(text_validation)
    # NGワード読み込みおわり


    # 前回データ削除はじまり
    path = './images'
    save.Delete_data()
    try:
      shutil.rmtree(path)
      os.mkdir(path)
    except FileNotFoundError:
      os.mkdir(path)
    # 前回データ削除終わり

    #Amazonからデータ取得
    search = get_page.get_data(search_url, int(search_number), int(stock), prime, float(review), together, *ng_word)
    #Amazonからデータ取得終わり
    return search


@eel.expose
def tabele():
  data = []
  record = []
  db_datas = save.Get_sql()
  p = 1;
  for row in db_datas:
    record.append(p)
    record.append(row[1])
    record.append(row[3])
    record.append(row[4])
    data.append(record)
    p = p + 1
    record = []
  return data


eel.init("web")
eel.start("index.html")