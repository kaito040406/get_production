import os, sys, time
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import tkinter.ttk as ttk
from get_production_data import get_page
from save_data import save
import shutil




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

def GetValueSearchConditions(event):
  search_url = EditBox2.get()
  search_number = EditBox3.get()
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
    int_search_number = int(search_number)
    search = get_page.get_data(search_url, int_search_number)
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
  root.filename =  filedialog.asksaveasfilename(initialdir = "/",title = "Save as",filetypes =  [("text file","*.csv")])
  with open(root.filename, 'w') as f:
    print("no." + "," +"ASIN" + "," + "title" + "," + "price" + "," + "url" + "" , file=f)
    p = 1
    for row in getting_data:
      print(str(p) + "," + row[1] + "," + row[3] + "," + row[4] + "," + row[2] + "" , file=f)
      p += 1
    f.close()



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
Button.place(x=550, y=190)

Button_export = tk.Button(root, text=u'エクスポート', fg='#333333', height=1, width=10)
Button_export.config(bg='red')
Button_export.bind("<Button-1>",Export_csv)
Button_export.place(x=630, y=740)

root.mainloop()