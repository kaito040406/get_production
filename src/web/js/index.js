onload = function () {
  document.getElementById("submit_button").onclick = function () {
    var result = confirm("実行しますか？");
    if (result) {
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
        insertz_table(array);
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
        var target = document.getElementById("first");
        // console.log(target);
        var i = 1;
        data.forEach(function (value) {
          var insert_data = document.createElement("tr");
          insert_data.id = "table" + String(i);

          var child_tr = table.appendChild(insert_data);
          // insert_data.id = "table" + String(i);
          // table.insertBefore(insert_data, target.nextSibling);
          var column = document.getElementById("table" + String(i));
          // targetelement = document.getElementById("table" + String(i));

          var nomber = document.createElement("th");
          nomber.id = "nomber" + String(i);
          nomber.textContent = value[0];
          var child_nomber = column.appendChild(nomber);
          // column.insertBefore(nomber, column.nextSibling);
          // column.insertBefore(nomber, column.firstChild);

          // target_nomber = document.getElementById("nomber" + String(i));
          var asin = document.createElement("th");
          asin.id = "asin" + String(i);
          asin.textContent = value[1];
          var child_asin = column.appendChild(asin);
          // column.insertBefore(asin, target_nomber.nextSibling);
          // column.insertBefore(asin, column.firstChild);

          // target_asin = document.getElementById("asin" + String(i));
          var title = document.createElement("th");
          title.id = "title" + String(i);
          title.textContent = value[2];
          var child_title = column.appendChild(title);
          // column.insertBefore(title, target_asin.nextSibling);
          // column.insertBefore(title, column.firstChild);

          // target_title = document.getElementById("title" + String(i));
          var price = document.createElement("th");
          price.id = "price" + String(i);
          price.textContent = value[3];
          var child_price = column.appendChild(price);
          // column.insertBefore(price, target_title.nextSibling);
          // column.insertBefore(price, column.firstChild);

          i = i + 1;
        });
      }
    }
  }
};
