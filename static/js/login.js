console.log("Running");
let loginForm = document.querySelector("#formLogin");
let loginButton = document.querySelector("#loginButton");
console.log(loginForm);
loginButton.addEventListener("click" , (e) => {
    e.preventDefault();
    let username = loginForm.user.value;
    let password = loginForm.password.value;
    if (username == "Demo" && password == "1234"){
        window.location.href = `/dashboard`;
    }
});