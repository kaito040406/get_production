from PIL import Image, ImageTk
from itertools import count
import threading
import tkinter as tk
from tkinter import messagebox


#処理画面を表示するクラス
class ImageLabel(tk.Label):
  def load(self, im):
    if isinstance(im, str):
      im = Image.open(im)
    self.loc = 0
    self.frames = []

    try:
      for i in count(1):
        self.frames.append(ImageTk.PhotoImage(im.copy()))
        im.seek(i)
    except EOFError:
      pass

    try:
      self.delay = im.info['duration']
    except:
      self.delay = 100

    if len(self.frames) == 1:
      self.config(image=self.frames[0])
    else:
      self.next_frame()

  def unload(self):
    self.config(image=None)
    self.frames = None

  def next_frame(self):
    if self.frames:
      self.loc += 1
      self.loc %= len(self.frames)
      self.config(image=self.frames[self.loc])
      self.after(self.delay, self.next_frame)


class gif_controller:
    
  def make_gif(self, root2):
    messagebox.showinfo('実行', '実行しますか？')
    self.canvas = tk.Canvas(root2, width=800, height=800, background="white")
    self.text = tk.Label(root2, text=u'取得中',font=(u'ＭＳ ゴシック', 28))
    self.lbl = ImageLabel(root2)
    self.canvas.place(x=0, y=0)
    self.text.place(x=370,y=300)
    self.lbl.pack()
    self.lbl.place(x=350,y=100)
    self.lbl.load('Preloader_8.gif')
    
    
  def status(self):
    self.lbl.destroy()
    self.canvas.destroy()

  def stop(self):
    self.status()