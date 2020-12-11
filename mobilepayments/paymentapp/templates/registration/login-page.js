const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    // url = 'https://cors-anywhere.herokuapp.com/https://u8fpqfk2d4.execute-api.ap-southeast-1.amazonaws.com/techtrek2020/login'
    // fetch(url).then(response => {
    //     return response.json();
    // })
    // .then(login=>{
    //     console.log(login);
    // })
    var myHeaders = new Headers();
    myHeaders.append("x-api-key", "WaiaCA14j19ibdk6JZR3D5E03Y8I21HQ3nDMh3c5");
    myHeaders.append("Content-Type", "text/plain");

    var raw = "{\n    \"username\": \"Group24\",\n    \"password\": \"EXDv_Kuy_5hKhxD\"\n}";

    var requestOptions = {
    method: 'POST',
    headers: myHeaders,
    body: raw,
    redirect: 'follow'
    };

    fetch("https://u8fpqfk2d4.execute-api.ap-southeast-1.amazonaws.com/techtrek2020/login", requestOptions)
    .then(response => response.text())
    .then(result => console.log(result))
    .catch(error => console.log('error', error));

    if (username === "user" && password === "web_dev") {
        alert("You have successfully logged in.");
        location.reload();
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})