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
  count = []
  tearm = []
  end_time = []
  image1 = []
  image2 = []
  image3 = []
  start_city = []
  shipping_cost = []
  payment = []
  yahoo = []
  bank_transfer = []
  easy_deal = []
  bank_id = []
  bank_name1 = []
  registeredmail = []
  cash_on_delivery = []
  condition = []
  returns = []
  buy_limit = []
  but_limit = []
  authentication_restrictions = []
  auto_extension = []
  early_termination = []
  price_reduction_negotiations = []
  automatic_relisting = []
  automatic_price_cut = []
  automatic_price_reduction_rate = []
  bold = []
  back_color = []
  icon = []
  shipping_fixed = []
  nekopos = []
  kuroneko = []
  yuu_packet = []
  yuu_pack = []
  hakoboon = []
  hakoboonmini = []
  lead_time = []
  shipping_method1 = []
  sipping_price = []
  after_searvice = []
  abroad = []
  afi = []
  befor_check = []
 

  bland_check = False
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

    for check in check_data:
      k = k + 1
      if str(row[8]) + str(row[9]) == check[2]:
        bland_check = True
        ct_id.append(check[0])
        title.append(row[3])
        insert_text = str(row[7]) + "◆支払詳細<br>【お支払い方法】 Yahoo!かんたん決済<br>【支払い代金】 落札価格 ＋ 送料<br>　※ 銀行振込希望の方は、Yahoo!かんたん決済の銀行振り込みをご利用ください。<br>　※ 直接の銀行振込みは、お断りしております。<br><br>◆発送詳細<br>【送料】 ★ 全国一律料金 ★<br>【発送までの日数】 お支払い完了後 1～2日で発送いたします。<br>【配送業者】 主にヤマト運輸、日本郵便、佐川急便から発送いたします。また別の業者を使うこともあります。<br><br>◆注意事項 ★必ずご確認ください★<br>・質問、メッセージの回答は夜になることが多いです。<br>・手渡しは対応しておりません。<br>・商品によって業者を変えるため【センター留め】【郵便局留め】は対応できません。<br>・領収書の同梱は対応しておりません。<br>・まとめて取引は、トラブルが多いためお断りしております。<br>・不具合以外での返品・交換は対応しておりません。<br>・Yahoo!かんたん決済の支払期限を過ぎた場合、落札者都合のキャンセルをいたします。"
        text.append(insert_text)
        start_price.append(str(row[4]))
        end_price_value = int(row[4]) + 200
        end_price.append(str(end_price_value))
        count.append(str(row[6]))
        tearm.append("")
        end_time.append("")
        image1.append(str(row[6]))
        image2.append("")
        image3.append("")
        start_city.append("東京都")
        shipping_cost.append("落札者")
        payment.append("先払い")
        yahoo.append("はい")
        bank_transfer.append("いいえ")
        easy_deal.append("はい")
        bank_id.append("")
        bank_name1.append("")
        registeredmail.append("")
        cash_on_delivery.append("")
        condition.append("新品、未使用")
        returns.append("")
        buy_limit.append("はい")
        but_limit.append("いいえ")
        authentication_restrictions.append("いいえ")
        auto_extension.append("はい")
        early_termination.append("はい")
        price_reduction_negotiations.append("いいえ")
        automatic_relisting.append("3")
        automatic_price_cut.append("いいえ")
        automatic_price_reduction_rate.append("")
        bold.append("いいえ")
        back_color.append("いいえ")
        icon.append("いいえ")
        shipping_fixed.append("はい")
        nekopos.append("いいえ")
        kuroneko.append("いいえ")
        yuu_packet.append("いいえ")
        yuu_pack.append("いいえ")
        hakoboon.append("いいえ")
        hakoboonmini.append("いいえ")
        lead_time.append("1日~2日")
        shipping_method1.append("宅急便（ヤマト運輸）")
        sipping_price.append("780")
        after_searvice.append("いいえ")
        abroad.append("いいえ")
        afi.append("いいえ")
        befor_check.append("いいえ")
        
  if bland_check == False:
    for row in output_data:
      for check in check_data:
        if str(row[8]) == check[2]:
          bland_check = True
          ct_id.append(check[0])
          title.append(row[3])
          insert_text = str(row[7]) + "◆支払詳細<br>【お支払い方法】 Yahoo!かんたん決済<br>【支払い代金】 落札価格 ＋ 送料<br>　※ 銀行振込希望の方は、Yahoo!かんたん決済の銀行振り込みをご利用ください。<br>　※ 直接の銀行振込みは、お断りしております。<br><br>◆発送詳細<br>【送料】 ★ 全国一律料金 ★<br>【発送までの日数】 お支払い完了後 1～2日で発送いたします。<br>【配送業者】 主にヤマト運輸、日本郵便、佐川急便から発送いたします。また別の業者を使うこともあります。<br><br>◆注意事項 ★必ずご確認ください★<br>・質問、メッセージの回答は夜になることが多いです。<br>・手渡しは対応しておりません。<br>・商品によって業者を変えるため【センター留め】【郵便局留め】は対応できません。<br>・領収書の同梱は対応しておりません。<br>・まとめて取引は、トラブルが多いためお断りしております。<br>・不具合以外での返品・交換は対応しておりません。<br>・Yahoo!かんたん決済の支払期限を過ぎた場合、落札者都合のキャンセルをいたします。"
          text.append(insert_text)
          start_price.append(str(row[4]))
          end_price_value = int(row[4]) + 200
          end_price.append(str(end_price_value))
          count.append(str(row[6]))
          tearm.append("")
          end_time.append("")
          image1.append(str(row[6]))
          image2.append("")
          image3.append("")
          start_city.append("東京都")
          shipping_cost.append("落札者")
          payment.append("先払い")
          yahoo.append("はい")
          bank_transfer.append("いいえ")
          easy_deal.append("はい")
          bank_id.append("")
          bank_name1.append("")
          registeredmail.append("")
          cash_on_delivery.append("")
          condition.append("新品、未使用")
          returns.append("")
          buy_limit.append("はい")
          but_limit.append("いいえ")
          authentication_restrictions.append("いいえ")
          auto_extension.append("はい")
          early_termination.append("はい")
          price_reduction_negotiations.append("いいえ")
          automatic_relisting.append("3")
          automatic_price_cut.append("いいえ")
          automatic_price_reduction_rate.append("")
          bold.append("いいえ")
          back_color.append("いいえ")
          icon.append("いいえ")
          shipping_fixed.append("はい")
          nekopos.append("いいえ")
          kuroneko.append("いいえ")
          yuu_packet.append("いいえ")
          yuu_pack.append("いいえ")
          hakoboon.append("いいえ")
          hakoboonmini.append("いいえ")
          lead_time.append("1日~2日")
          shipping_method1.append("宅急便（ヤマト運輸）")
          sipping_price.append("780")
          after_searvice.append("いいえ")
          abroad.append("いいえ")
          afi.append("いいえ")
          befor_check.append("いいえ")

  return_data.append(ct_id)
  return_data.append(title)
  return_data.append(text)
  return_data.append(start_price)
  return_data.append(end_price)
  return_data.append(count)
  return_data.append(tearm)
  return_data.append(end_time)
  return_data.append(image1)
  return_data.append(image2)
  return_data.append(image3 )
  return_data.append(start_city) 
  return_data.append(shipping_cost) 
  return_data.append(payment)
  return_data.append(yahoo) 
  return_data.append(bank_transfer) 
  return_data.append(easy_deal) 
  return_data.append(bank_id) 
  return_data.append(bank_name1) 
  return_data.append(registeredmail) 
  return_data.append(cash_on_delivery) 
  return_data.append(condition) 
  return_data.append(returns) 
  return_data.append(buy_limit) 
  return_data.append(but_limit) 
  return_data.append(authentication_restrictions) 
  return_data.append(auto_extension) 
  return_data.append(early_termination) 
  return_data.append(price_reduction_negotiations) 
  return_data.append(automatic_relisting) 
  return_data.append(automatic_price_cut) 
  return_data.append(automatic_price_reduction_rate)
  return_data.append(bold) 
  return_data.append(back_color) 
  return_data.append(icon) 
  return_data.append(shipping_fixed) 
  return_data.append(nekopos) 
  return_data.append(kuroneko) 
  return_data.append(yuu_packet) 
  return_data.append(yuu_pack) 
  return_data.append(hakoboon) 
  return_data.append(hakoboonmini) 
  return_data.append(lead_time) 
  return_data.append(shipping_method1) 
  return_data.append(sipping_price)
  return_data.append(after_searvice)
  return_data.append(abroad)
  return_data.append(afi)
  return_data.append(befor_check)


  output_data = []
  for i in range(len(return_data[0])):
    tmp = []
    for v in return_data:
      tmp.append(v[i])
    output_data.append(tmp)

  return output_data
  # print(output_data)
  # if len(output_data) == 0:
  #   return False
  # else:     
  #   now = datetime.datetime.now().strftime('%Y%m%d%H%M')
  #   root.filename =  filedialog.asksaveasfilename(initialfile=str(now) ,initialdir = "/",title = "Save as",filetypes =  [("text file","*.csv")])
  #   with open(root.filename, 'w') as f:
  #     print("カテゴリ" + "," +"タイトル" + "," + "説明" + "," + "開始価格" + "," + "即決価格" + "," +"個数" + "," + "開催期間" + "," + "終了期間" + "," + "画像１" + "," + "画像２" + "," + "画像３" + "," + "商品発送元の都道府県" + "," + "送料負担" + "," + "代金支払い" + "," + "Yahoo!かんたん決済" + "," + "銀行振込" + "," + "かんたん取引" + "," + "銀行ID" + "," + "銀行名１" + "," + "現金書留" + "," + "商品代引" + "," + "商品の状態" + "," + "返品の可否" + "," + "入札者評価制限" + "," + "自動延長" + "," + "早期終了" + "," + "値下げ交渉" + "," + "自動再出品" + "," + "自動値下げ" + "," + "自動値下げ価格変動率" + "," + "太字テキスト" + "," + "背景色" + "," + "贈答品アイコン" + "," + "送料固定" + "," + "ネコポス" + "," + "ネコ宅急便コンパクト" + "," + "ネコ宅急便" + "," + "ゆうパケット" + "," + "ゆうパック" + "," + "はこBOON" + "," + "はこBOONmini" + "," + "発送までの日数" + "," + "発送方法１" + "," + "発送方法１全国一律価格" + "," + "受け取り後決済サービス" + "," + "海外発送" + "," + "アフィリエイト" + "," + "出品者情報開示前チェック", file=f)
  #     p = 1
  #     for row in output_data:
  #       print(row[0] + "," + row[1] + "," + row[2] + "," + row[3] + "," + row[4] + "," + row[5] + "," + row[6] + "," + row[7] + "," + row[8] + "," + row[9] + "," + row[10] + "," + row[11] + "," + row[12] + "," + row[13] + "," + row[14] + "," + row[15] + "," + row[16] + "," + row[17] + "," + row[18] + "," + row[19] + "," + row[20] + "," + row[21] + "," + row[22] + "," + row[23] + "," + row[24] + "," + row[25] + "," + row[26] + "," + row[27] + "," + row[28] + "," + row[29] + "," + row[30] + "," + row[31] + "," + row[32] + "," + row[33] + "," + row[34] + "," + row[35] + "," + row[36] + "," + row[37] + "," + row[38] + "," + row[39] + "," + row[40] + "," + row[41] + "," + row[42] + "," + row[43] + "," + row[44] + "," + row[45] + "," + row[46] + "," + row[47] + "," + row[48], file=f)
  #       p += 1
  #     f.close()
  #     # ０から４8
  #   return True