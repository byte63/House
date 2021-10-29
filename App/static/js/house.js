function CheckUser(email) {
  alert("fffff");
  $.ajax({
    url: 'http://127.0.0.1:5000/check_user',
    type: 'post',
    data: {"user_name": email},
    dataType: 'format',
    success: function (response) {
      console.log(email)
    }
  })
}
