onload = function () {
  document.getElementById("submit_button").onclick = function () {
    var search_ward = document.getElementById("search_ward").value;
    var members = document.getElementById("members").value;
    var counts = document.getElementById("counts").value;
    var prime_flag = false;
    var w_but_flag = false;

    if (document.form.prime.checked) {
      prime_flag = true;
    }
    if (document.form.w_buy.checked) {
      w_but_flag = true;
    }

    console.log(search_ward);
    console.log(members);
    console.log(counts);
    console.log(prime_flag);
    console.log(w_but_flag);
  };
};
