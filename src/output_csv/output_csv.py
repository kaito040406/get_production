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
  count = "1"
  tearm = "1"
  end_time = "22"
  image1 = []
  image2 = ""
  image3 = ""
  start_city = "東京都"
  shipping_cost = "落札者"
  payment = "先払い"
  yahoo = "はい"
  bank_transfer = "いいえ"
  easy_deal = "はい"
  bank_id = ""
  bank_name1 = ""
  registeredmail = ""
  cash_on_delivery = ""
  condition = "新品、未使用"
  returns = ""
  buy_limit = "はい"
  but_limit = "いいえ"
  authentication_restrictions = "いいえ"
  auto_extension = "はい"
  early_termination = "はい"
  price_reduction_negotiations = "いいえ"
  automatic_relisting = 3
  automatic_price_cut = "いいえ"
  automatic_price_reduction_rate = ""
  bold = "いいえ"
  back_color = "いいえ"
  icon = "いいえ"
  shipping_fixed = "はい"
  nekopos = "いいえ"
  kuroneko = "いいえ"
  yuu_packet = "いいえ"
  yuu_pack = "いいえ"
  hakoboon = "いいえ"
  hakoboonmini = "いいえ"
  lead_time = "1日~2日"
  shipping_method1 = "宅急便（ヤマト運輸）"
  sipping_price = "780"
  after_searvice = "いいえ"
  abroad = "いいえ"
  afi = "いいえ"
  befor_check = "いいえ"

  bland_check = False
  
  test_ct = "家電＆カメラ ? カメラ ? デジタルカメラ ? デジタル一眼 ? ミラーレス一眼"
  with open("category.csv") as f:
    reader = csv.reader(f)
    for row in output_data:
      for check in reader:
        # 本来は以下
        # if str(row[8]) + str(row[9]) == check[5]:
        if test_ct == check[5]:
          bland_check = True
          ct_id.append(check[0])
          title.append(row[3])
          insert_text = str(row[7]) + "◆支払詳細<br>【お支払い方法】 Yahoo!かんたん決済<br>【支払い代金】 落札価格 ＋ 送料<br>　※ 銀行振込希望の方は、Yahoo!かんたん決済の銀行振り込みをご利用ください。<br>　※ 直接の銀行振込みは、お断りしております。<br><br>◆発送詳細<br>【送料】 ★ 全国一律料金 ★<br>【発送までの日数】 お支払い完了後 1～2日で発送いたします。<br>【配送業者】 主にヤマト運輸、日本郵便、佐川急便から発送いたします。また別の業者を使うこともあります。<br><br>◆注意事項 ★必ずご確認ください★<br>・質問、メッセージの回答は夜になることが多いです。<br>・手渡しは対応しておりません。<br>・商品によって業者を変えるため【センター留め】【郵便局留め】は対応できません。<br>・領収書の同梱は対応しておりません。<br>・まとめて取引は、トラブルが多いためお断りしております。<br>・不具合以外での返品・交換は対応しておりません。<br>・Yahoo!かんたん決済の支払期限を過ぎた場合、落札者都合のキャンセルをいたします。"
          text.append(insert_text)
          start_price.append(str(row[7]))
          end_price.append(str(int(row[4] + 200)))
          image1.append(str(row[6]))

          return_data.append(
                        ct_id
                        ,title
                        ,text
                        ,start_price
                        ,end_price
                        ,count
                        ,tearm
                        ,end_time
                        ,image1
                        ,image2
                        ,image3 
                        ,start_city 
                        ,shipping_cost 
                        ,payment 
                        ,yahoo 
                        ,bank_transfer 
                        ,easy_deal 
                        ,bank_id 
                        ,bank_name1 
                        ,registeredmail 
                        ,cash_on_delivery 
                        ,condition 
                        ,returns 
                        ,buy_limit 
                        ,but_limit 
                        ,authentication_restrictions 
                        ,auto_extension 
                        ,early_termination 
                        ,price_reduction_negotiations 
                        ,automatic_relisting 
                        ,automatic_price_cut 
                        ,automatic_price_reduction_rate 
                        ,bold 
                        ,back_color 
                        ,icon 
                        ,shipping_fixed 
                        ,nekopos 
                        ,kuroneko 
                        ,yuu_packet 
                        ,yuu_pack 
                        ,hakoboon 
                        ,hakoboonmini 
                        ,lead_time 
                        ,shipping_method1 
                        ,sipping_price
                        ,after_searvice
                        ,abroad
                        ,afi
                        ,befor_check
                      )
    if bland_check == False:
      for row in output_data:
        for check in reader:
          # 本来は以下
          # if str(row[8]) == check[5]:
          if test_ct == check[5]:
            bland_check = True
            ct_id.append(check[0])
            title.append(row[3])
            insert_text = str(row[7]) + "◆支払詳細<br>【お支払い方法】 Yahoo!かんたん決済<br>【支払い代金】 落札価格 ＋ 送料<br>　※ 銀行振込希望の方は、Yahoo!かんたん決済の銀行振り込みをご利用ください。<br>　※ 直接の銀行振込みは、お断りしております。<br><br>◆発送詳細<br>【送料】 ★ 全国一律料金 ★<br>【発送までの日数】 お支払い完了後 1～2日で発送いたします。<br>【配送業者】 主にヤマト運輸、日本郵便、佐川急便から発送いたします。また別の業者を使うこともあります。<br><br>◆注意事項 ★必ずご確認ください★<br>・質問、メッセージの回答は夜になることが多いです。<br>・手渡しは対応しておりません。<br>・商品によって業者を変えるため【センター留め】【郵便局留め】は対応できません。<br>・領収書の同梱は対応しておりません。<br>・まとめて取引は、トラブルが多いためお断りしております。<br>・不具合以外での返品・交換は対応しておりません。<br>・Yahoo!かんたん決済の支払期限を過ぎた場合、落札者都合のキャンセルをいたします。"
            text.append(insert_text)
            start_price.append(str(row[7]))
            end_price.append(str(int(row[4] + 200)))
            image1.append(str(row[6]))

            return_data.append(
                          ct_id
                          ,title
                          ,text
                          ,start_price
                          ,end_price
                          ,count
                          ,tearm
                          ,end_time
                          ,image1
                          ,image2
                          ,image3 
                          ,start_city 
                          ,shipping_cost 
                          ,payment 
                          ,yahoo 
                          ,bank_transfer 
                          ,easy_deal 
                          ,bank_id 
                          ,bank_name1 
                          ,registeredmail 
                          ,cash_on_delivery 
                          ,condition 
                          ,returns 
                          ,buy_limit 
                          ,but_limit 
                          ,authentication_restrictions 
                          ,auto_extension 
                          ,early_termination 
                          ,price_reduction_negotiations 
                          ,automatic_relisting 
                          ,automatic_price_cut 
                          ,automatic_price_reduction_rate 
                          ,bold 
                          ,back_color 
                          ,icon 
                          ,shipping_fixed 
                          ,nekopos 
                          ,kuroneko 
                          ,yuu_packet 
                          ,yuu_pack 
                          ,hakoboon 
                          ,hakoboonmini 
                          ,lead_time 
                          ,shipping_method1 
                          ,sipping_price
                          ,after_searvice
                          ,abroad
                          ,afi
                          ,befor_check
                        )
      f.close()      
    return return_data
      
      