import os, sys, time
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import tkinter.ttk as ttk
import shutil
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_binary




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


def GetValueSearchConditions(event):
  options = Options()
  driver = webdriver.Chrome(chrome_options=options)
  url = "https://www.google.co.jp/"
  driver.get(url)
  search_url = EditBox2.get()
  time.sleep(3)
  element = driver.find_element_by_class_name("gLFyf")
  print(driver.find_element_by_class_name("gLFyf"))
  element.send_keys(search_url)
  element.submit()
  time.sleep(3)
  cur_url = driver.current_url
  print(cur_url)
  driver.quit()


Static1 = tk.Label(root, text=u'自動取得アプリ', font=(u'ＭＳ ゴシック', 25))
Static1.place(x=320, y=10)
Static1.config(bg='#CCFFCC')

Static2 = tk.Label(root, text=u'商品検索URL', font=(u'ＭＳ ゴシック', 18))
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

root.mainloop()