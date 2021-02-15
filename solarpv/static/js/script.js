//Validation Code for Inputs

var username = document.forms['form']['username'];
var password = document.forms['form']['password'];

var uname_error = document.getElementById('uname_error');
var psw_error = document.getElementById('psw_error');

username.addEventListener('textInput', username_Verify);
password.addEventListener('textInput', password_Verify);

function validated() {
  if (username.value.length < 3) {
    username.style.border = "1px solid red";
    uname_error.style.display = "block";
    username.focus();
    return false;
  }
  if (password.value.length < 3) {
    password.style.border = "1px solid red";
    psw_error.style.display = "block";
    password.focus();
    return false;
  }
}

function username_Verify() {
  if (username.value.length >= 3) {
    username.style.border = "1px solid silver";
    uname_error.style.display = "none";
    return false;
  }
}

function password_Verify() {
  if (password.value.length >= 3) {
    password.style.border = "1px solid silver";
    psw_error.style.display = "none";
    return false;
  }
}
