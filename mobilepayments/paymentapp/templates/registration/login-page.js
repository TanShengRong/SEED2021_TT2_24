const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    url = 'https://cors-anywhere.herokuapp.com/https://u8fpqfk2d4.execute-api.ap-southeast-1.amazonaws.com/techtrek2020/login'
    fetch(url, {
        method: "POST",
        headers: {
            'x-api-key': "WaiaCA14j19ibdk6JZR3D5E03Y8I21HQ3nDMh3c5",
        },
        body: JSON.stringify({
            custID: 7,
        })
    }).then(response => {
        return response.json();
    })
    .then(login=>{
        console.log(login);
    })

    if (username === login.user && password === login.password) {
        alert("You have successfully logged in.");
        location.replace("./balance.html");
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})