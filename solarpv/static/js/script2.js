//Validation Code for Inputs

var fname = document.forms['form']['fname'];
var email = document.forms['form']['email'];
var subject = document.forms['form']['subject'];

var fname_error = document.getElementById('fname_error');
var email_error = document.getElementById('email_error');
var subject_error = document.getElementById('subject_error');

fname.addEventListener('textInput', fname_Verify);
email.addEventListener('textInput', email_Verify);
subject.addEventListener('textInput', subject_Verify);

function validated() {
  if (fname.value.length < 3) {
    fname.style.border = "1px solid red";
    fname_error.style.display = "block";
    fname.focus();
    return false;
  }
  if (email.value.length < 6) {
    email.style.border = "1px solid red";
    email_error.style.display = "block";
    email.focus();
    return false;
  }
  if (subject.value.length < 1) {
    subject.style.border = "1px solid red";
    subject_error.style.display = "block";
    subject.focus();
    return false;
  }

}

function fname_Verify() {
  if (fname.value.length >= 3) {
    fname.style.border = "1px solid silver";
    fname_error.style.display = "none";
    return false;
  }
}

function email_Verify() {
  if (email.value.length >= 6) {
    email.style.border = "1px solid silver";
    email_error.style.display = "none";
    return false;
  }
}

function subject_Verify() {
  if (subject.value.length >= 1) {
    subject.style.border = "1px solid silver";
    subject_error.style.display = "none";
    return false;
  }
}
