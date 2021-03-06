onload = function () {
  document.getElementById("submit_button").onclick = function () {
    var result = confirm("実行しますか？");
    if (result) {
      make_gif();
      data_submit();
    } else {
      alert("キャンセルされました");
    }
  };

  function data_submit() {
    var search_ward = document.getElementById("search_ward").value; //検索ワード
    var members = document.getElementById("members").value; //検索数
    var counts = document.getElementById("counts").value; //最低在庫数
    var review = document.getElementById("review").value; //最低レビュー
    var prime_flag = false; //プライム消費のみをとるか？
    var w_but_flag = false; //あわせがいをブロックするか？

    //プライム消費のみをとるかのチェックボックスの状態確認
    if (document.form.prime.checked) {
      prime_flag = true;
    }
    //合わせがいをブロックするかのチェックボックスの状態確認
    if (document.form.w_buy.checked) {
      w_but_flag = true;
    }

    pysub();

    async function pysub() {
      var check = await eel.start(
        search_ward,
        members,
        counts,
        review,
        prime_flag,
        w_but_flag
      )();
      alert("終わりました");
      if (check == true) {
        var array = await eel.tabele()();
        delete_gif(); //処理中画面削除
        insertz_table(array); //テーブル表示
      } else {
        var error = document.getElementById("error_message_box");
        try {
          var child = document.getElementById("e_message");
          error.removeChild(child);
        } catch (e) {}
        var liFirst = document.createElement("li");
        liFirst.id = "e_message";
        liFirst.textContent = "正しい情報を入力してください";
        error.insertBefore(liFirst, error.firstChild);
      }
      function insertz_table(data) {
        table = document.getElementById("table");
        var i = 1;
        data.forEach(function (value) {
          var insert_data = document.createElement("tr");
          insert_data.id = "table" + String(i);
          table.appendChild(insert_data);
          var column = document.getElementById("table" + String(i));

          var nomber = document.createElement("th");
          nomber.id = "nomber" + String(i);
          nomber.textContent = value[0];
          column.appendChild(nomber);

          var asin = document.createElement("th");
          asin.id = "asin" + String(i);
          asin.textContent = value[1];
          column.appendChild(asin);

          var title = document.createElement("th");
          title.id = "title" + String(i);
          title.textContent = value[2];
          column.appendChild(title);

          var price = document.createElement("th");
          price.id = "price" + String(i);
          price.textContent = value[3];
          column.appendChild(price);

          i = i + 1;
        });
      }
    }
  }

  function make_gif() {
    var target_elemet = document.getElementById("gif_box");
    target_elemet.style.display = "block";
  }
  function delete_gif() {
    var target_elemet = document.getElementById("gif_box");
    target_elemet.style.display = "none";
  }
  document.getElementById("export_button").onclick = function () {
    alert("ファイルを出力します");
    cav_output();
  };
  async function cav_output() {
    var csv_data = await eel.out_csv()();
    if (csv_data.length == 0) {
      alert("出力できるデータはありません");
    } else {
      var now = new Date();
      var Year = now.getFullYear();
      var Month = now.getMonth() + 1;
      var Day = now.getDate();
      var Hour = now.getHours();
      var Min = now.getMinutes();
      var Sec = now.getSeconds();
      var now =
        String(Year) +
        String(Month) +
        String(Day) +
        String(Hour) +
        String(Min) +
        String(Sec);
      //名前がバグる
      download(arrToCSV(csv_data), now);
    }
  }

  function download(data, name) {
    const bom = "\uFEFF";

    const blob = new Blob([bom, data], { type: "text/csv" });
    const anchor = document.createElement("a");
    anchor.download = name;
    anchor.href = window.URL.createObjectURL(blob);
    document.body.appendChild(anchor);
    anchor.click();
    anchor.parentNode.removeChild(anchor);
  }

  function arrToCSV(arr) {
    return arr
      .map((row) => {
        return row.map((str) => {
          return '"' + (str ? str.replace(/"/g, '""') : "") + '"';
        });
      })
      .map((row) => {
        return row.join(",");
      })
      .join("\n");
  }
};
