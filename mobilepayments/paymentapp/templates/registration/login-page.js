const loginForm = document.getElementById("login-form");
const loginButton = document.getElementById("login-form-submit");
const loginErrorMsg = document.getElementById("login-error-msg");

loginButton.addEventListener("click", (e) => {
    e.preventDefault();
    const username = loginForm.username.value;
    const password = loginForm.password.value;

    url = 'https://cors-anywhere.herokuapp.com/https://u8fpqfk2d4.execute-api.ap-southeast-1.amazonaws.com/techtrek2020/login'
    fetch(url).then(response => {
        return response.json();
    })
    .then(login=>{
        console.log(login);
    })
    


    if (username === "user" && password === "web_dev") {
        alert("You have successfully logged in.");
        location.reload();
    } else {
        loginErrorMsg.style.opacity = 1;
    }
})