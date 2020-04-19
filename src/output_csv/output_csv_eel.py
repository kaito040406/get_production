import csv
import datetime
import sqlite3

dbname = "production.db"

def Out_csv(*output_data):
  return_data = []
  ct_id = []
  title = []
  text = []
  start_price = []
  end_price = []
  image1 = []
  sipping_price = []
 
  i = 0
  k = 0
  check_data = []
  with open("category.csv") as f:
    reader = csv.reader(f)
    for check in reader:
      check_data.append(check)
    f.close()

  for row in output_data:
    i=i+1
    k = k + 1
    ct_id.append(row[8])
    title.append(row[3])
    insert_text = str(row[7]) + "◆支払詳細\r【お支払い方法】 Yahoo!かんたん決済r【支払い代金】 落札価格 ＋ 送料\r　※ 銀行振込希望の方は、Yahoo!かんたん決済の銀行振り込みをご利用ください。\r　※ 直接の銀行振込みは、お断りしております。\r\r◆発送詳細\r【送料】 ★ 全国一律料金 ★\r【発送までの日数】 お支払い完了後 1～2日で発送いたします。\r【配送業者】 主にヤマト運輸、日本郵便、佐川急便から発送いたします。また別の業者を使うこともあります。\r\r◆注意事項 ★必ずご確認ください★\r・質問、メッセージの回答は夜になることが多いです。\r・手渡しは対応しておりません。\r・商品によって業者を変えるため【センター留め】【郵便局留め】は対応できません。\r・領収書の同梱は対応しておりません。\r・まとめて取引は、トラブルが多いためお断りしております。\r・不具合以外での返品・交換は対応しておりません。\r・Yahoo!かんたん決済の支払期限を過ぎた場合、落札者都合のキャンセルをいたします。"
    text.append(insert_text)
    start_price.append(str(int(row[4]) + 100))
    end_price_value = int(int(row[4]) + 100 + 200)
    end_price.append(str(end_price_value))
    image1.append(str(row[6]))
    sipping_price.append("780")

  return_data.append(ct_id)
  return_data.append(title)
  return_data.append(text)
  return_data.append(start_price)
  return_data.append(end_price)
  return_data.append(image1)
  return_data.append(sipping_price)
  output_data = []
  for i in range(len(return_data[0])):
    tmp = []
    for v in return_data:
      tmp.append(v[i])
    output_data.append(tmp)

  return output_data