const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    var myHeaders = new Headers();
    myHeaders.append("x-api-key", "WaiaCA14j19ibdk6JZR3D5E03Y8I21HQ3nDMh3c5");
    myHeaders.append("Content-Type", "text/plain");
    // ===for testing
    // var username1 = "Group24"; var password1 = "EXDv_Kuy_5hKhxD";
    // ===for testing
    var tmp = {
        username: username,
        password: password,
    }
    var raw = JSON.stringify(tmp)

    var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
    };

    fetch("https://u8fpqfk2d4.execute-api.ap-southeast-1.amazonaws.com/techtrek2020/login", requestOptions)
    .then(function (response) {
        if (response.status == 200) {
            console.log('success')
            alert("You have successfully logged in.");
            location.replace(".Balance/balance.html");
            // return response.json(); // for checking purpose
        } else { loginErrorMsg.style.opacity = 1; }
    })
    // .then(result => console.log(result)) //show credentials
    .catch(error => console.log('error', error));
})