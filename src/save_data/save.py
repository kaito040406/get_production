
import sqlite3
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
      image01
    );
    """
    c.execute(ddl)
    c.close()
  except sqlite3.OperationalError:
    pass


def Save_data(number, asin, url, title, price, image):
  c = sqlite3.connect(dbname)
  sql_insert = """
  insert into production (asin, url, title, price, image) values (?, ?, ?, ?, ?);
  """
  insert_list = (asin, url, title, price)
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
