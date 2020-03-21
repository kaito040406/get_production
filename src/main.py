import os, sys, time
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import tkinter.ttk as ttk
from get_production_data import get_page
from save_data import save
import shutil
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from output_csv import output_csv
import chromedriver_binary
import csv
import datetime


def GetValueSearchConditions(event):

  # ブラウザ操作
  options = Options()
  driver = webdriver.Chrome(chrome_options=options)
  url = "https://www.amazon.co.jp/"
  driver.get(url)
  search_word = EditBox2.get()
  time.sleep(3)
  element = driver.find_element_by_id("twotabsearchtextbox")
  element.send_keys(search_word)
  element.submit()
  search_url = driver.current_url
  time.sleep(0.5)
  driver.quit()
  time.sleep(0.5)
  # ブラウザ操作


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

  search_number = EditBox3.get()
  if float(search_number) <= 0:
    messagebox.showinfo('エラー', '1以上を入力してください')
    EditBox2.delete(0,tk.END)
    EditBox3.delete(0,tk.END)
  else:
    try:
      # 前回データ削除はじまり
      tree.delete(*tree.get_children())
      path = './images'
      save.Delete_data()
      try:
        shutil.rmtree(path)
        os.mkdir(path)
      except FileNotFoundError:
        os.mkdir(path)
      # 前回データ削除終わり

      # Amazonからデータ取得はじまり
      search = get_page.get_data(search_url, int(search_number), combo_stock.get(), prime.get(), combo_review.get(), together.get(), *ng_word)
      messagebox.showinfo('報告', search)
      # Amazonからデータ取得おわり

      #レコード取得はじまり
      db_datas = save.Get_sql()
      p = 1
      for row in db_datas:
        tree.insert("","end", tags=p, values=(p,row[1],row[3],row[4]))
        if p & 1:
          tree.tag_configure(p,background="#DDDDDD")
        p += 1
      #レコード取得おわり

    except ValueError:
      messagebox.showinfo('エラー', '数字を入力してください')
      EditBox2.delete(0,tk.END)
      EditBox3.delete(0,tk.END)



def Export_csv(event):
  getting_data =  save.Get_sql()
  save_check = output_csv.Out_csv(root, *getting_data)
  if save_check == True:
    messagebox.showinfo('完了', '正しく出力できました')
  else:
    messagebox.showinfo('エラー', '出力できるデータはありません')  



# Save_title
save.Save_title()

# dbname = "production_data.db"
root = tk.Tk()
root.title(u"Get Production")
root.geometry("800x1000")
root.configure(bg='#CCFFCC')

tree = ttk.Treeview(root)
style = ttk.Style()
style.configure("Treeview", font=(None, 13), rowheight=42)
style.configure("Treeview.Heading", font=(None, 15))
tree["columns"] = (1,2,3,4)
tree["show"] = "headings"
tree.column(1,width=50)
tree.column(2,width=120)
tree.column(3,width=380)
tree.column(4,width=100)
tree.heading(1,text="No.")
tree.heading(2,text="ASIN")
tree.heading(3,text="タイトル")
tree.heading(4,text="金額")
tree.place(x=75, y=270)


Static1 = tk.Label(root, text=u'自動取得アプリ', font=(u'ＭＳ ゴシック', 25))
Static1.place(x=320, y=10)
Static1.config(bg='#CCFFCC')

Static2 = tk.Label(root, text=u'検索ワード', font=(u'ＭＳ ゴシック', 18))
Static2.place(x=100, y=70)
Static2.config(bg='#CCFFCC')

EditBox2 = tk.Entry(root, width=45)
EditBox2.place(x=230, y=70)


Static3 = tk.Label(root, text=u'取得件数', font=(u'ＭＳ ゴシック', 18))
Static3.place(x=100, y=110)
Static3.config(bg='#CCFFCC')

EditBox3 = tk.Entry(root, width=10)
EditBox3.place(x=230, y=110)


Button = tk.Button(root, text=u'実行', fg='#333333', height=2, width=10)
Button.config(bg='red')
Button.bind("<Button-1>",GetValueSearchConditions)
Button.place(x=550, y=200)

Button_export = tk.Button(root, text=u'エクスポート', fg='#333333', height=1, width=10)
Button_export.config(bg='red')
Button_export.bind("<Button-1>",Export_csv)
Button_export.place(x=630, y=740)


label1 = tk.Label(root, text=u"最低在庫数",font=(u'ＭＳ ゴシック', 18),bg='#CCFFCC')
label1.place(x=100, y=150)

combo_stock = ttk.Combobox(root, state='readonly',width=6)
combo_stock["values"] = (1,2,3,4,5,6,7,8,9,10)
combo_stock.current(4)
combo_stock.place(x=230, y=150)

label2 = tk.Label(root, text=u"最低レビュー",font=(u'ＭＳ ゴシック', 18),bg='#CCFFCC')
label2.place(x=100, y=190)

combo_review = ttk.Combobox(root, state='readonly',width=6)
combo_review["values"] = (1.0,2.0,3.0,4.0,5.0)
combo_review.current(2)
combo_review.place(x=230, y=190)


prime  = tk.BooleanVar()
prime.set(True)
prime_check = tk.Checkbutton(root, variable=prime ,text='primeのみ取得',font=(u'ＭＳ ゴシック', 15),bg='#CCFFCC')
prime_check.place(x=330, y=150)


together = tk.BooleanVar()
together.set(True)
together_check = tk.Checkbutton(root, variable=prime ,text='合わせ買いブロック',font=(u'ＭＳ ゴシック', 15),bg='#CCFFCC')
together_check.place(x=470, y=150)

root.mainloop()