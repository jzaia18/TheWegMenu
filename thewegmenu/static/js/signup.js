var p1 = $("#password_input")[0];
var p2 = $("#confirm_password_input")[0];
var button = $("#submit_form")[0];

function validate() {
  if (p1.value == p2.value && p1.value.length >= 5) {
    button.disabled = false;
  }
  else {
    button.disabled = true;
  }
}

p1.addEventListener('blur', validate);
p2.addEventListener('blur', validate);
p1.addEventListener('input', validate);
p2.addEventListener('input', validate);
