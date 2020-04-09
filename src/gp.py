import eel

@eel.expose
def start():
  print("ooo")

eel.init("web")
eel.start("index.html")