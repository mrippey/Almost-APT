// Get the container element
var btnContainer = document.getElementById("sidebar-wrapper");

// Get all buttons with class="btn" inside the container
var btns = btnContainer.getElementsByClassName("btn");

// Loop through the buttons and add the active class to the current/clicked button
for (var i = 0; i < btns.length; i++) {
  btns[i].addEventListener("click", function() {
    var current = document.getElementsByClassName("active");
    current[0].className = current[0].className.replace(" active", "");
    this.className += " active";
  });
}
//https://www.w3schools.com/howto/howto_js_validation_empty_input.asp
function validateForm() {
  var x = document.forms["search"]["search"].value;
  if (x == "") {
    alert("Please enter a search term before submitting");
    return false;
  }
}