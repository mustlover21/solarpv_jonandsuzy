$(document).ready(function () {



  // Validate Username
  $('#usercheck').hide();
  let usernameError = true;
  $('#usernames').keyup(function () {
      validateUsername();
  });

  function validateUsername() {
    let usernameValue = $('#usernames').val();
    if (usernameValue.length == '') {
      $('#usercheck').show();
          usernameError = false;
          return false;
    }
    else if((usernameValue.length < 3)||
            (usernameValue.length > 8)) {
      $('#usercheck').show();
      $('#usercheck').html
("**Length of username must be between 3 and 8 characters");
      usernameError = false;
      return false;
    }
    else {
      $('#usercheck').hide();
    }
  }

 // Validate Email
  const email = document.getElementById('email');
    email.addEventListener('blur', ()=>{
      let regex =
/^([_\-\.0-9a-zA-Z]+)@([_\-\.0-9a-zA-Z]+)\.([a-zA-Z]){2,7}$/;
      let s = email.value;
      if(regex.test(s)){
        email.classList.remove(
              'is-invalid');
        emailError = true;
    } else {
      email.classList.add(
            'is-invalid');
      emailError = false;
    }
  })

 // Validate Password
  $('#passcheck').hide();
  let passwordError = true;
  let regex =
/^(?=.{3,8}$)(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])/;
  $('#password').keyup(function () {
      validatePassword();
  });
  function validatePassword() {
    let passwrdValue =
        $('#password').val();
    if (passwrdValue.length == '') {
        $('#passcheck').show();
        passwordError = false;
        return false;
    }
    if (!regex.test(passwrdValue)) {
      $('#passcheck').show();
      $('#passcheck').html
("**Password must be between 3-8 characters, and contain at least 1 lowercase character, uppercase character, and a digit");
      $('#passcheck').css("color", "red");
      passwordError = false;
      return false;
    } else {
      $('#passcheck').hide();
    }
  }

// Validate Confirm Password
  $('#conpasscheck').hide();
  let confirmPasswordError = true;
  $('#conpassword').keyup(function () {
      validateConfirmPasswrd();
  });
  function validateConfirmPasswrd() {
    let confirmPasswordValue =
      $('#conpassword').val();
    let passwrdValue =
      $('#password').val();
    if (passwrdValue != confirmPasswordValue) {
      $('#conpasscheck').show();
      $('#conpasscheck').html(
            "**Password does not match");
      $('#conpasscheck').css(
            "color", "red");
      confirmPasswordError = false;
      return false;
    } else {
      $('#conpasscheck').hide();
    }
  }

  // Submitt button
  $('#submitbtn').click(function () {
    validateUsername();
    validatePassword();
    validateConfirmPasswrd();
    validateEmail();
    if ((usernameError == true) &&
        (passwordError == true) &&
        (confirmPasswordError == true) &&
        (emailError == true)) {
        return true;
    } else {
        return false;
    }
  });
});
