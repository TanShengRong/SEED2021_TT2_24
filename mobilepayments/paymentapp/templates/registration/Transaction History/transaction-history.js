var raw = JSON.stringify({"custID":24});

      var requestOptions = {
      method: 'POST',
      headers: myHeaders,
      body: raw,
      redirect: 'follow'
      };

      fetch("https://u8fpqfk2d4.execute-api.ap-southeast-1.amazonaws.com/techtrek2020/transaction/view", requestOptions)
      .then(response => response.text())
      .then(function(result) {
        var obj = JSON.parse(result);
        document.getElementById("cur-balance-details").innerHTML = "Balance in the account is $" + obj[0].availableBal;
        document.getElementById("multi-balance-details").innerHTML = "Balance in the account is $" + obj[1].availableBal;
        document.getElementById("savings-balance-details").innerHTML = "Balance in the account is $" + obj[2].availableBal;
      })
      .catch(error => console.log('error', error));

const transferButton = document.getElementById("transfer-form-submit");

loginButton.addEventListener("click", (e) => {
    location.replace(".Tranfer/transfer.html");
})