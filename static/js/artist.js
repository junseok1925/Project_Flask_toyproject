$(document).ready(function () {
    set_temp();
    show_comment();
  });
  function set_temp() {
    fetch("http://spartacodingclub.shop/sparta_api/weather/seoul").then((res) => res.json()).then((data) => {
      console.log(data)
    });
  }
  function save_comment() {
    let formData = new FormData();
    formData.append("sample_give", "샘플데이터");

    fetch('/guestbook', { method: "POST", body: formData, }).then((res) => res.json()).then((data) => {
      //console.log(data)
      alert(data["msg"]);
    });
  }
  function show_comment() {
    fetch('/guestbook').then((res) => res.json()).then((data) => {
      alert(data["msg"])
    })
  }