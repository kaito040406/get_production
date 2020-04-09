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
    var check = eel.start(
      search_ward,
      members,
      counts,
      review,
      prime_flag,
      w_but_flag
    )();
    if (check == true) {
    } else {
      error();
    }
  }

  function error() {
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
};
