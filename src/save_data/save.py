
import sqlite3
import urllib.error
import urllib.request


dbname = "production.db"

def Save_title():
  c = sqlite3.connect(dbname)
  try:
    c.execute("PRAGMA foreign_keys = 1")
    ddl = """
    CREATE TABLE production
    (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      asin,
      url,
      title,
      price,
      image01,
      quentity,
      text
    );
    """
    c.execute(ddl)
    c.close()
  except sqlite3.OperationalError:
    pass


def Save_data(number, asin, url, title, price, image, quentity, text):
  c = sqlite3.connect(dbname)
  sql_insert = """
  insert into production (asin, url, title, price, image01, quentity, text) values (?, ?, ?, ?, ?, ?, ?);
  """
  insert_list = (asin, url, title, price, image, quentity, text)
  c.execute(sql_insert, insert_list)
  c.commit()
  c.close()


def Get_sql():
  c = sqlite3.connect(dbname)
  sql_get = """
  select * from production;
  """
  return  c.execute(sql_get)


def Delete_data():
  c = sqlite3.connect(dbname)
  sql_del = """
  delete from production;
  """
  c.execute(sql_del)
  c.commit()
  c.close()


def Image_download(url, nomber):
  dst_path = "images/"+ "image" +str(nomber)
  try:
    with urllib.request.urlopen(url) as web_file:
      data = web_file.read()
      with open(dst_path, mode='wb') as local_file:
        local_file.write(data)
    image = "image" +str(nomber)
    return image

  except urllib.error.URLError as e:
    print(e)
    image = "error"
    return image
  
  
